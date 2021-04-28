import time

from config.config import constants, autoDelete, autoRun, downloadServer
from functions.fs.createClientFolders import createClientFolders
from functions.getters.getAssets import getAssets
from functions.getters.getVersionData import getVersionData
from functions.getters.getVersionManifest import getVersionManifest
from functions.getters.getClient import getClient
from functions.getters.getServer import getServer
from functions.getters.getLibraries import getLibraries
from functions.getters.getNatives import getNatives
from functions.selectors.selectVersion import selectVersion
from functions.selectors.selectVersionType import selectVersionType
from functions.meta.createAutorunScript import createAutorunScript, run
from datetime import datetime
import shutil
import os


def build():
    # Получаем манифест всех версий minecraft.
    versionsInfo = getVersionManifest()
    # Выбираем тип выпуска minecraft.
    versions, versionsNumbs, versionType = selectVersionType(versionsInfo)
    # Выбираем номер версии, и получаем versionData.
    versionData = getVersionData(selectVersion(versions, versionsNumbs))
    # Создание всех нужных директорий и поддиректорий.
    createClientFolders(versionData)
    # # Загрузка клиента.
    getClient(versionData)
    # Загрузка сервера, если в config.py стоит True на параметре загрузки.
    if downloadServer:
        getServer(versionData)
    # Загрузка библиотек.
    getLibraries(versionData)
    # Загрузка нативов.
    getNatives(versionData)
    # Загрузка ассетов.
    magicImpotantMushrooms = getAssets(versionData)
    # Создание скрипта запуска.
    createAutorunScript(versionData['id'], versionData['assetIndex']['id'], versionType, magicImpotantMushrooms)

    print(f'\n| {datetime.now().time()} Сборка клиента завершена! |')


def main():
    print('|  Python minecraft client generator 1.0  |\n')

    if os.path.exists(constants['package']['outputPath']):
        if autoDelete:
            print('Удаление старого клиента... Три секунды на спасение дома...')
            time.sleep(3)
            print('Прощай, дом!')
            shutil.rmtree('output')
        else:
            print(
                "Директория с клиентом уже существует. Клиент будет запущен без скачивания (если включено в конфиге). Даём секунду на подумать..."
            )
            time.sleep(1)
            if autoRun:
                run()
            return
    build()


if __name__ == '__main__':
    main()
