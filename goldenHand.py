from functions.fs.createClientFolders import createClientFolders
from functions.getters.getAssets import getAssets
from functions.getters.getVersionData import getVersionData
from functions.getters.getVersionManifest import getVersionManifest
from functions.getters.getClient import getClient
from functions.getters.getLibraries import getLibraries
from functions.getters.getNatives import getNatives
from functions.selectors.selectVersion import selectVersion
from functions.selectors.selectVersionType import selectVersionType
from datetime import datetime

if __name__ == '__main__':
    print('|  GreatRay client generator 0.1  |\n')

    # Получаем манифест всех версий minecraft
    versionsInfo = getVersionManifest()
    # Выбираем тип выпуска minecraft
    versions, versionsNumbs = selectVersionType(versionsInfo)
    # Выбираем номер версии, и получаем versionData
    versionData = getVersionData(selectVersion(versions, versionsNumbs))
    # Создание всех нужных директорий и поддиректорий
    createClientFolders(versionData)
    # Загрузка клиента
    getClient(versionData)
    # Загрузка библиотек
    getLibraries(versionData)
    # Загрузка нативов
    getNatives(versionData)
    # Загрузка ассетов
    getAssets(versionData)

    print(f'| {datetime.now().time()} Сборка клиента завершена! |')

    # TODO сделать автоматическую генерацию скрипта запуска
