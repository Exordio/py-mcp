from functions.network.request import request
from config.config import constants
from datetime import datetime


def getVersionManifest():
    print(f'| {datetime.now().time()} Получаем манифест версий |')
    versionManifest = request(constants['api']['versionsInfo'], json=True)
    print(f'| {datetime.now().time()} Манифест получен |\n')
    return versionManifest
