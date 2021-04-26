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


def request(url, json = False, content = False):
    if json:
        return requests.get(url).json()
    if content:
        return requests.get(url).content


def download(url, dest, size, visibleName):
    pass



def getVersionManifest():
    return request(constants['api']['versionsInfo'], json=True)


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
    print(versionsNumbs)
    print('| Введите номер версии для сборки клиента |')

    finded = False
    while not finded:
        versionSelect = input(' : ')
        for i in versionsNumbs:
            if i == versionSelect:
                print('Версия найдена')
                finded = True
                break
        if not finded:
            print('Версия не найдена, повторите ввод.')

    for i in versions:
        if i['id'] == versionSelect:
            versionData = i



    versionData = request(versionData['url'], json=True)
    print(versionData['downloads']['client']['url'].split('/')[-1])

    with open(f'''{constants['package']['outputPath']}/{versionData['downloads']['client']['url'].split('/')[-1]}''', 'wb') as vsd:
        vsd.write(request(versionData['downloads']['client']['url'], content=True))











