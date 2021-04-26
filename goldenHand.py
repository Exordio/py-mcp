import requests
import os

from datetime import datetime

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
    for lib in vd['libraries']:
        if 'natives' in lib:
            continue
        if not 'rules' in lib:
            librariesByVersionInfo.append(lib['downloads']['artifact'])
            continue

        for rule in lib['rules']:
            if rule['action'] == 'allow':
                if 'os' in rule:
                    if rule['os']['name'] != 'osx':
                        librariesByVersionInfo.append(lib['downloads']['artifact'])

    print(f'| {datetime.now().time()} Формирование списка закачки библиотек |')
    print(librariesByVersionInfo)
    print(f'| {datetime.now().time()} Список сформирован, начинаем загрузку |\n')

    LBVIDownloadCounter = len(librariesByVersionInfo) - 1

    for lib in librariesByVersionInfo:
        downloadFile(lib['url'], lib['url'].split('/')[-1], f'''{constants['package']['outputPath']}/{constants['package']['librariesDir']}''', LBVIDownloadCounter)
        LBVIDownloadCounter -= 1


def getNatives(vd):
    nativesByVersionInfo = []
    for lib in vd['libraries']:
        if 'natives' in lib:
            if platform in lib['natives']:
                nativesByVersionInfo.append(lib['downloads']['classifiers'][lib['natives'][platform]])

    print(nativesByVersionInfo)

    NBVIDownloadCounter = len(nativesByVersionInfo) - 1

    for native in nativesByVersionInfo:




if __name__ == '__main__':
    print('|  GreatRay client generator 0.1  |\n')
    print(f'| {datetime.now().time()} Предварительно создаём новую папку для генерации клиента |')

    try:
        os.mkdir(constants['package']['outputPath'])
    except FileExistsError:
        print(f'| {datetime.now().time()} Папка уже создана |')

    print(f'| {datetime.now().time()} Получаем манифест версий |')
    versionsInfo = getVersionManifest()

    print(f'| {datetime.now().time()} Манифест получен |\n')
    versions = []
    versionsNumbs = []

    for i in versionsInfo['versions']:
        if i['type'] == 'release':
            versions.append(i)
            versionsNumbs.append(i['id'])

    versionData = getVersionData(selectVersion(versionsNumbs))
    # Получаем клиент
    getClient(versionData)

    print(f'\n| {datetime.now().time()} Создаем папку для библиотек |')
    try:
        os.mkdir(f'''{constants['package']['outputPath']}/{constants['package']['librariesDir']}''')
    except FileExistsError:
        print(f'| {datetime.now().time()} Папка уже создана |\n')

    getLibraries(versionData)

    print(f'\n| {datetime.now().time()} Создаем папку для нативов |')
    try:
        os.mkdir(f'''{constants['package']['outputPath']}/{constants['package']['nativesDir']}''')
    except FileExistsError:
        print(f'| {datetime.now().time()} Папка уже создана |\n')



    getNatives(versionData)



