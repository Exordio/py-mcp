from functions.network.downloadFile import downloadFile
from config.config import constants


def getServer(vd):
    downloadFile(vd['downloads']['server']['url'], vd['downloads']['server']['url'].split('/')[-1], constants['package']['outputPath'])
