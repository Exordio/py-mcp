from functions.fs.createClientFolders import createClientFolders
from functions.getters.getAssets import getAssets
from functions.getters.getVersionData import getVersionData
from functions.selectors.selectVersion import selectVersion
from functions.getters.getVersionManifest import getVersionManifest
from functions.getters.getClient import getClient
from functions.getters.getLibraries import getLibraries
from functions.getters.getNatives import getNatives
from functions.selectors.selectVersionType import selectVersionType
from datetime import datetime

if __name__ == '__main__':
    print('|  GreatRay client generator 0.1  |\n')

    print(f'| {datetime.now().time()} Получаем манифест версий |')
    versionsInfo = getVersionManifest()
    print(f'| {datetime.now().time()} Манифест получен |\n')

    versions, versionsNumbs = selectVersionType(versionsInfo)

    versionData = getVersionData(selectVersion(versions, versionsNumbs))

    createClientFolders(versionData)

    getClient(versionData)
    getLibraries(versionData)
    getNatives(versionData)
    getAssets(versionData)

    print(f'| {datetime.now().time()} Сборка клиента завершена! |')
