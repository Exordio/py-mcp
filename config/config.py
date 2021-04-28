constants = {
    'api': {
        'versionsInfo': 'https://launchermeta.mojang.com/mc/game/version_manifest.json',
        'assetsDownloadBaseUrl': 'http://resources.download.minecraft.net',
    },
    'package': {
        'outputPath': './output',
        'tmpPath': './output/tmp',
        'librariesDir': 'libraries',
        'assetsDir': 'assets',
        'nativesDir': 'natives',
    },
}

# Установка платфомы windows, linux, osx.
platform = 'windows'
# Ставаить True, если нужно автоматически запустить клиент, после сборки.
autoRun = True
# Ставить True, если нужно перекачивать файлы каждый раз при запуске скрипта.
autoDelete = True
# Ставить True, усли нужно скачать server.
# Иногда у какой то версии нет сервера.
# Выход - либо завернуть в try except, вызов закачки сервера, либо поставить тут False.
downloadServer = False
