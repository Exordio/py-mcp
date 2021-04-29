from functions.network.request import request
from config.config import constants

import json
import ast
import os


def getAssets(vd):
    assetsResponse = request(vd['assetIndex']['url'], content=True)
    with open(f'''{constants['package']['outputPath']}/{constants['package']['assetsDir']}/indexes/{vd['assetIndex']['id']}.json''', 'wb') as file:
        file.write(assetsResponse)
    try:
        assets = ast.literal_eval(assetsResponse.decode('utf-8'))['objects']
    except ValueError:
        assets = json.loads(assetsResponse.decode('utf-8'))['objects']
    assetDownloadLinks = {}

    # For up to version 1.6 inclusive...
    very_important = 'READ_ME_I_AM_VERY_IMPORTANT' in assets or 'READ_ME_I_AM_VERY_IMPORTANT.txt' in assets

    # This is for the 1.6 version.
    # Who wrote the assembly of the client for the launcher obviously very, very much ate mushrooms
    very_important_new = 'READ_ME_I_AM_VERY_IMPORTANT.txt' in assets

    for asset in assets:
        assetHash = assets[asset]['hash']
        assetHashSlice = assetHash[0:2]
        assetFileSave = assetHash
        assetDir = f'''{constants['package']['outputPath']}/{constants['package']['assetsDir']}/objects/{assetHashSlice}'''
        if very_important:
            dirname = os.path.dirname(asset)
            if len(dirname) > 0:
                dirname = f'/{dirname}'
            if very_important_new:
                assetDir = f'''{constants['package']['outputPath']}/{constants['package']['assetsDir']}{dirname}'''
            else:
                assetDir = f'''{constants['package']['outputPath']}/data/.minecraft/resources{dirname}'''
            assetFileSave = os.path.basename(asset)
        assetDownloadUrl = f'''{constants['api']['assetsDownloadBaseUrl']}/{assetHashSlice}/{assetHash}'''

        if not os.path.exists(assetDir):
            os.makedirs(assetDir, exist_ok=True)

        assetDownloadLinks[f'''{assetDir}/{assetFileSave}'''] = {'url': assetDownloadUrl, 'unpack': False}

    # Do not ask me about it... Mojang programmers consume mushrooms on an industrial scale XD
    return 'READ_ME_I_AM_VERY_IMPORTANT' in assets, assetDownloadLinks
