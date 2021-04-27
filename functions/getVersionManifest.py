from functions.request import request
from config.config import constants


def getVersionManifest():
    return request(constants['api']['versionsInfo'], json=True)
