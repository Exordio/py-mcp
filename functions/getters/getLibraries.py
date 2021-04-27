from functions.network.downloadFile import downloadFile
from datetime import datetime
from config.config import constants

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
    print(librariesByVersionInfo)
    print(f'| {datetime.now().time()} Список сформирован, начинаем загрузку |\n')

    LBVIDownloadCounter = len(librariesByVersionInfo) - 1

    for lib in librariesByVersionInfo:
        downloadFile(lib['url'], lib['url'].split('/')[-1], f'''{constants['package']['outputPath']}/{constants['package']['librariesDir']}''', LBVIDownloadCounter)
        LBVIDownloadCounter -= 1

