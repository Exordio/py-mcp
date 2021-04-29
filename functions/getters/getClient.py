from config.config import constants


def getClient(vd):
    return {f'''{constants['package']['outputPath']}/{vd['downloads']['client']['url'].split('/')[-1]}''': {'url': vd['downloads']['client']['url'], 'unpack': False}}
