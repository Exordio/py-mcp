from functions.network.asyncPoolDownloader import runAsyncDownloader
from functions.getters.getAssets import getAssets
from functions.getters.getClient import getClient
from functions.getters.getServer import getServer
from functions.getters.getLibraries import getLibraries
from functions.getters.getNatives import getNatives
from config.config import downloadServer
from datetime import datetime

import selectors
import asyncio


def doSomeAsyncMagic(vd):
    magicImportantMushrooms, downloadPool = createDownloadPool(vd)
    selector = selectors.SelectSelector()
    loop = asyncio.SelectorEventLoop(selector)
    asyncio.set_event_loop(loop)
    loop.run_until_complete(runAsyncDownloader(downloadPool))

    print(f'\n| {datetime.now().time()} All downloads done! |\n')
    return magicImportantMushrooms


def createDownloadPool(vd):
    magicImportantMushrooms, assetDownloadPool = getAssets(vd)
    serverDownloadPool = {}
    # If the config specifies to download the server
    if downloadServer:
        serverDownloadPool = getServer(vd)
    # de facto approach in merging dictionaries, if u run this on python 3.9+ u can do it with new union operator |
    # downloadDict = assetDownloadPool | getClient(vd) | getServer(vd) | serverDownloadPool etc..
    downloadDict = {**assetDownloadPool, **getClient(vd), **serverDownloadPool, **getLibraries(vd), **getNatives(vd)}

    return magicImportantMushrooms, downloadDict
