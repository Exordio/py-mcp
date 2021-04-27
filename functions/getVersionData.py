from functions.request import request


def getVersionData(commonVersionData):
    return request(commonVersionData['url'], json=True)
