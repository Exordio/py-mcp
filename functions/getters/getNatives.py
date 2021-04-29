from config.config import constants, platform


def getNatives(vd):
    nativesByVersionInfo = []
    for lib in vd['libraries']:
        if 'natives' in lib:
            if platform in lib['natives']:
                try:
                    nativesByVersionInfo.append(lib['downloads']['classifiers'][lib['natives'][platform]])
                except KeyError:
                    try:
                        nativesByVersionInfo.append(lib['downloads']['classifiers']['natives-windows'])
                    except KeyError:
                        try:
                            nativesByVersionInfo.append(lib['downloads']['classifiers'][
                                                            'natives-windows-64' if platform == 'windows' else 'natives-linux'])
                        except KeyError:
                            nativesByVersionInfo.append(lib['downloads']['classifiers'][
                                                            'natives-osx'])

    nativesByVersionInfoDict = {}
    for native in nativesByVersionInfo:
        nativesByVersionInfoDict[
            f'''{constants['package']['outputPath']}/{constants['package']['nativesDir']}/{native['url'].split('/')[-1]}'''] = {
            'url': native['url'], 'unpack': True}

    return nativesByVersionInfoDict

