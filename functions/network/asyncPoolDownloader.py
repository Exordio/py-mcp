import asyncio
import aiohttp
import os

from zipfile import ZipFile
from config.config import constants


async def fetch(objMeta, session, path):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
    try:
        async with session.get(
                objMeta['url'], headers=headers,
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

            # For unpack natives
            if objMeta['unpack']:
                try:
                    with ZipFile(
                            f'''{constants['package']['outputPath']}/{constants['package']['nativesDir']}/{objMeta['url'].split('/')[-1]}''',
                            'r') as zipObj:
                        zipObj.extractall(f'''{constants['package']['outputPath']}/{constants['package']['nativesDir']}''')
                    os.remove(
                        f'''{constants['package']['outputPath']}/{constants['package']['nativesDir']}/{objMeta['url'].split('/')[-1]}''')
                except FileNotFoundError:
                    pass

            return (objMeta['url'], 'OK', content)
    except Exception as e:
        print(e)
        return (objMeta['url'], 'ERROR', str(e))


async def runAsyncDownloader(pathList):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for path in pathList:
            task = asyncio.ensure_future(fetch(pathList[path], session, path))
            tasks.append(task)
        responses = asyncio.gather(*tasks)
        await responses
    return responses
