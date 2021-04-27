from functions.network.downloadFile import downloadFile
from config.config import constants


def getClient(vd):
    downloadFile(vd['downloads']['client']['url'], vd['downloads']['client']['url'].split('/')[-1], constants['package']['outputPath'])
