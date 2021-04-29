from config.config import constants


def getServer(vd):
    return {f'''{constants['package']['outputPath']}/{vd['downloads']['server']['url'].split('/')[-1]}''': {'url': vd['downloads']['server']['url'], 'unpack': False}}
