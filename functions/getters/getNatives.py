import shutil
import os

from datetime import datetime
from zipfile import ZipFile

from functions.network.downloadFile import downloadFile
from config.config import constants, platform


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
