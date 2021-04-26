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


def getClient(vd):
    print(f'''| {datetime.now().time()} Загружаем {vd['downloads']['client']['url'].split('/')[-1]} |''')
    with open(f'''{constants['package']['outputPath']}/{vd['downloads']['client']['url'].split('/')[-1]}''',
              'wb') as vsd:
        vsd.write(request(vd['downloads']['client']['url'], content=True))

    print(f'''| {datetime.now().time()} Загружен {vd['downloads']['client']['url'].split('/')[-1]} |''')


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
            print('Версия не найдена, повторите ввод.')

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
            print(rule)
            print(lib)
            # if rule['action'] == 'allow' and rule['os']['name'] == platform:
                # librariesByVersionInfo.append(lib['downloads']['artifact'])

    print(librariesByVersionInfo)


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


    # sv = selectVersion(versionsNumbs)

    versionData = getVersionData(selectVersion(versionsNumbs))

    print(versionData['libraries'])

    # Получаем клиент
    getClient(versionData)

    print(f'| {datetime.now().time()} Создаем папку для библеотек |')
    try:
        os.mkdir(f'''{constants['package']['outputPath']}/{constants['package']['librariesDir']}''')
    except FileExistsError:
        print(f'| {datetime.now().time()} Папка уже создана |')

    getLibraries(versionData)


