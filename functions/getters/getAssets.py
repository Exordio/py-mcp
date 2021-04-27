import aiohttp
import asyncio
import json
import ast
import os

from functions.network.request import request
from config.config import constants
from datetime import datetime


def getAssets(vd):
    print(f'\n| {datetime.now().time()} Начинаем загрузку ассетов |\n')

    async def fetch(url, session, path):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
        try:
            async with session.get(
                    url, headers=headers,
                    ssl=False,
                    timeout=aiohttp.ClientTimeout(
                        total=None,
                        sock_connect=10,
                        sock_read=10
                    )
            ) as response:
                content = await response.read()
                print(path)
                with open(path, 'wb') as file:
                    file.write(content)

                return (url, 'OK', content)
        except Exception as e:
            print(e)
            return (url, 'ERROR', str(e))

    async def run(url_list):
        tasks = []
        async with aiohttp.ClientSession() as session:
            for url in url_list:
                task = asyncio.ensure_future(fetch(url_list[url], session, url))
                tasks.append(task)
            responses = asyncio.gather(*tasks)
            await responses
        return responses

    assetsResponse = request(vd['assetIndex']['url'], content=True)
    with open(f'''{constants['package']['outputPath']}/{constants['package']['assetsDir']}{vd['id']}/indexes/{vd['assetIndex']['id']}.json''', 'wb') as file:
        file.write(assetsResponse)

    print(assetsResponse)
    # print((assetsResponse.decode('utf-8'))['objects'])
    try:
        assets = ast.literal_eval(assetsResponse.decode('utf-8'))['objects']
    except ValueError:
        assets = json.loads(assetsResponse.decode('utf-8'))['objects']
    assetDownloadLinks = {}

    print(assets)
    for asset in assets:
        assetHash = assets[asset]['hash']
        assetHashSlice = assetHash[0:2]
        assetDir = f'''{constants['package']['outputPath']}/{constants['package']['assetsDir']}{vd['id']}/objects/{assetHashSlice}'''
        assetDownloadUrl = f'''{constants['api']['assetsDownloadBaseUrl']}/{assetHashSlice}/{assetHash}'''

        if not os.path.exists(assetDir):
            os.mkdir(assetDir)

        assetDownloadLinks[f'''{assetDir}/{assetHash}'''] = assetDownloadUrl

    asyncio.run(run(assetDownloadLinks))

    print('\n| Загрузка ассетов завершена. |')
