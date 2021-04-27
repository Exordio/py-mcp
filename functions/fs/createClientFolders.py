import os

from config.config import constants


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
            f'''{constants['package']['outputPath']}/{constants['package']['assetsDir']}/indexes''')
    except FileExistsError:
        pass