from functions.selectors.selectVersion import selectVersion
from functions.selectors.selectVersionType import selectVersionType
from functions.getters.getVersionData import getVersionData
from functions.getters.getVersionManifest import getVersionManifest
from functions.fs.createClientFolders import createClientFolders
from functions.meta.createAutorunScript import createAutorunScript
from functions.meta.asyncMagic import doSomeAsyncMagic
from config.config import constants
from datetime import datetime

import shutil


def build():
    versionsInfo = getVersionManifest()
    versions, versionsNumbs, versionType = selectVersionType(versionsInfo)
    versionData = getVersionData(selectVersion(versions, versionsNumbs))
    createClientFolders(versionData)
    magicImportantMushrooms = doSomeAsyncMagic(versionData)
    shutil.rmtree(f'''{constants['package']['outputPath']}/{constants['package']['nativesDir']}/META-INF''')
    createAutorunScript(versionData['id'], versionData['assetIndex']['id'], versionType, magicImportantMushrooms)

    print(f'\n| {datetime.now().time()} Complete! |')
