from functions.network.request import request
from config.config import constants
from datetime import datetime


def getVersionManifest():
    print(f'| {datetime.now().time()} Getting the version manifest |')
    versionManifest = request(constants['api']['versionsInfo'], json=True)
    print(f'| {datetime.now().time()} Manifest received |\n')
    return versionManifest
