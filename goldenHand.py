from functions.createClientFolders import createClientFolders
from functions.getAssets import getAssets
from functions.getVersionData import getVersionData
from functions.selectVersion import selectVersion
from functions.getVersionManifest import getVersionManifest
from functions.getClient import getClient
from functions.getLibraries import getLibraries
from functions.getNatives import getNatives
from functions.selectVersionType import selectVersionType
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
