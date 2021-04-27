import time

from config.config import constants, autoRun
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
import os

if __name__ == '__main__':
    print('|  Exord minecraft client generator 0.1  |\n')

    if os.path.exists(constants['package']['outputPath']):
        print("Директория с клиентом уже существует. Клиент будет запущен без скачивания (если включено в конфиге). Даём 3 секунды на подумать...")
        time.sleep(3)
        if autoRun:
            run()
    else:
        # Получаем манифест всех версий minecraft
        versionsInfo = getVersionManifest()
        # Выбираем тип выпуска minecraft
        versions, versionsNumbs, versionType = selectVersionType(versionsInfo)
        # Выбираем номер версии, и получаем versionData
        versionData = getVersionData(selectVersion(versions, versionsNumbs))
        # Создание всех нужных директорий и поддиректорий
        createClientFolders(versionData)
        # # Загрузка клиента
        getClient(versionData)
        # Загрузка сервера
        getServer(versionData)
        # Загрузка библиотек
        getLibraries(versionData)
        # Загрузка нативов
        getNatives(versionData)
        # Загрузка ассетов
        getAssets(versionData)
        # Создание скрипта запуска
        createAutorunScript(versionData['id'], versionData['assetIndex']['id'], versionType)

        print(f'\n| {datetime.now().time()} Сборка клиента завершена! |')
