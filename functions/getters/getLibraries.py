from config.config import constants


def getLibraries(vd):
    librariesByVersionInfo = []
    for lib in vd['libraries']:
        if 'natives' in lib:
            continue
        if not 'rules' in lib:
            librariesByVersionInfo.append(lib['downloads']['artifact'])
            continue

        for rule in lib['rules']:
            if rule['action'] == 'allow':
                if 'os' in rule:
                    continue
                else:
                    librariesByVersionInfo.append(lib['downloads']['artifact'])
    librariesByVersionInfoDict = {}
    for lib in librariesByVersionInfo:
        librariesByVersionInfoDict[
            f'''{constants['package']['outputPath']}/{constants['package']['librariesDir']}/{lib['url'].split('/')[-1]}'''] = {
            'url': lib['url'], 'unpack': False}
    return librariesByVersionInfoDict
