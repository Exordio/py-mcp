import requests
import asyncio
import aiohttp
import shutil
import ast
import os

from datetime import datetime
from zipfile import ZipFile


constants = {
    'api': {
        'versionsInfo': 'https://launchermeta.mojang.com/mc/game/version_manifest.json',
        'assetsDownloadBaseUrl': 'http://resources.download.minecraft.net',
    },
    'package': {
        'outputPath': './output',
        'tmpPath': './output/tmp',
        'librariesDir': 'libraries',
        'assetsDir': 'assets',
        'nativesDir': 'natives',
    },
}

platform = 'windows'

def request(url, json=False, content=False):
    if json:
        return requests.get(url).json()
    if content:
        return requests.get(url).content


def getVersionManifest():
    return request(constants['api']['versionsInfo'], json=True)


def downloadFile(url, filename, dist, count=0):
    with open(f'''{dist}/{filename}''', 'wb') as file:
        file.write(request(url, content=True))

    print(f'''| Загружен {filename} : Осталось {count} файлов |''')


def getClient(vd):
    downloadFile(vd['downloads']['client']['url'], vd['downloads']['client']['url'].split('/')[-1], constants['package']['outputPath'])


def selectVersion(vn):
    print(vn)
    print('| Введите номер версии для сборки клиента |')
    finded = False
    while not finded:
        versionSelect = input(' : ')
        for i in versionsNumbs:
            if i == versionSelect:
                print('| Версия найдена |')
                finded = True
                break
        if not finded:
            print('| Версия не найдена, повторите ввод. |')

    for i in versions:
        if i['id'] == versionSelect:
            return i


def getVersionData(commonVersionData):
    return request(commonVersionData['url'], json=True)


def getLibraries(vd):
    librariesByVersionInfo = []
    print(f'| {datetime.now().time()} Формирование списка загрузки библиотек |')
    for lib in vd['libraries']:
        if 'natives' in lib:
            continue
        if not 'rules' in lib:
            librariesByVersionInfo.append(lib['downloads']['artifact'])
            continue

        for rule in lib['rules']:
            if rule['action'] == 'allow':
                if 'os' in rule:
                     continue
                else:
                    librariesByVersionInfo.append(lib['downloads']['artifact'])

    print(vd['libraries'])
    print(librariesByVersionInfo)
    print(f'| {datetime.now().time()} Список сформирован, начинаем загрузку |\n')

    LBVIDownloadCounter = len(librariesByVersionInfo) - 1

    for lib in librariesByVersionInfo:
        downloadFile(lib['url'], lib['url'].split('/')[-1], f'''{constants['package']['outputPath']}/{constants['package']['librariesDir']}''', LBVIDownloadCounter)
        LBVIDownloadCounter -= 1


def getNatives(vd):
    nativesByVersionInfo = []
    print(f'| {datetime.now().time()} Формирование списка загрузки нативов |')
    for lib in vd['libraries']:
        if 'natives' in lib:
            if platform in lib['natives']:
                nativesByVersionInfo.append(lib['downloads']['classifiers'][lib['natives'][platform]])

    print(nativesByVersionInfo)
    print(f'| {datetime.now().time()} Список сформирован, начинаем загрузку |\n')

    NBVIDownloadCounter = len(nativesByVersionInfo) - 1

    for native in nativesByVersionInfo:
        downloadFile(native['url'], native['url'].split('/')[-1], f'''{constants['package']['outputPath']}/{constants['package']['nativesDir']}''', NBVIDownloadCounter)
        NBVIDownloadCounter -= 1

    print(f'\n| {datetime.now().time()} Начинаем распаковку нативов |\n')
    for native in nativesByVersionInfo:
        print(f'''| {datetime.now().time()} Распаковка {native['url'].split('/')[-1]} |''')
        with ZipFile(f'''{constants['package']['outputPath']}/{constants['package']['nativesDir']}/{native['url'].split('/')[-1]}''', 'r') as zipObj:
            zipObj.extractall(f'''{constants['package']['outputPath']}/{constants['package']['nativesDir']}''')

        os.remove(f'''{constants['package']['outputPath']}/{constants['package']['nativesDir']}/{native['url'].split('/')[-1]}''')

    shutil.rmtree(f'''{constants['package']['outputPath']}/{constants['package']['nativesDir']}/META-INF''')
    print(f'\n| {datetime.now().time()} Распаковка нативов завершена |\n')


def getAssets(vd):

    print(f'\n| {datetime.now().time()} Начинаем загрузку ассетов |\n')
    async def fetch(url, session, path):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
        try:
            async with session.get(
                    url, headers=headers,
                    ssl=False,
                    timeout=aiohttp.ClientTimeout(
                        total=None,
                        sock_connect=10,
                        sock_read=10
                    )
            ) as response:
                content = await response.read()
                print(path)
                with open(path, 'wb') as file:
                    file.write(content)

                return (url, 'OK', content)
        except Exception as e:
            print(e)
            return (url, 'ERROR', str(e))

    async def run(url_list):
        tasks = []
        async with aiohttp.ClientSession() as session:
            for url in url_list:
                task = asyncio.ensure_future(fetch(url_list[url], session, url))
                tasks.append(task)
            responses = asyncio.gather(*tasks)
            await responses
        return responses

    assetsResponse = request(vd['assetIndex']['url'], content=True)
    with open(f'''{constants['package']['outputPath']}/{constants['package']['assetsDir']}{vd['id']}/indexes/{vd['assetIndex']['id']}.json''', 'wb') as file:
        file.write(assetsResponse)

    assets = ast.literal_eval(assetsResponse.decode('utf-8'))['objects']

    assetDownloadLinks = {}

    print(assets)
    for asset in assets:
        assetHash = assets[asset]['hash']
        assetHashSlice = assetHash[0:2]
        assetDir = f'''{constants['package']['outputPath']}/{constants['package']['assetsDir']}{vd['id']}/objects/{assetHashSlice}'''
        assetDownloadUrl = f'''{constants['api']['assetsDownloadBaseUrl']}/{assetHashSlice}/{assetHash}'''

        if not os.path.exists(assetDir):
            os.mkdir(assetDir)

        assetDownloadLinks[f'''{assetDir}/{assetHash}'''] = assetDownloadUrl

    asyncio.run(run(assetDownloadLinks))

    print('\n| Загрузка ассетов завершена. |')

def createClientFolders(vd):
    # Создаём папку для вывода скрипта
    try:
        os.mkdir(constants['package']['outputPath'])
    except FileExistsError:
        pass

    # Создание папки для библиотек
    try:
        os.mkdir(f'''{constants['package']['outputPath']}/{constants['package']['librariesDir']}''')
    except FileExistsError:
        pass

    # Создание папок для нативов.
    try:
        os.mkdir(f'''{constants['package']['outputPath']}/{constants['package']['nativesDir']}''')
    except FileExistsError:
        pass

    # Создаем папки для ассетов
    try:
        os.makedirs(
            f'''{constants['package']['outputPath']}/{constants['package']['assetsDir']}{vd['id']}/indexes''')
    except FileExistsError:
        pass
    try:
        os.makedirs(
            f'''{constants['package']['outputPath']}/{constants['package']['assetsDir']}{vd['id']}/objects''')
    except FileExistsError:
        pass


if __name__ == '__main__':
    print('|  GreatRay client generator 0.1  |\n')
    print(f'| {datetime.now().time()} Получаем манифест версий |')
    versionsInfo = getVersionManifest()
    print(f'| {datetime.now().time()} Манифест получен |\n')
    versions = []
    versionsNumbs = []

    print('| Выберете версионную ветку для загрузки (Указать можно цифрой) |')
    print('1. Release\n2. Snapshot\n')
    typeSelected = False
    while not typeSelected:
        versionType = input(' : ')
        if versionType == '1':
            versionType = 'release'
            typeSelected = True
        elif versionType == '2':
            versionType = 'snapshot'
            typeSelected = True
        else:
            print('| Введено неверное значение, повторите ввод |')

    for i in versionsInfo['versions']:
        if i['type'] == versionType:
            versions.append(i)
            versionsNumbs.append(i['id'])

    versionData = getVersionData(selectVersion(versionsNumbs))

    createClientFolders(versionData)

    getClient(versionData)
    getLibraries(versionData)
    getNatives(versionData)
    getAssets(versionData)
