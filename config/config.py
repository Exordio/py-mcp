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

# Installation of the windows, linux, osx platform.
platform = 'windows'
# Set to True if you want to automatically start the client after building.
autoRun = True
# Set True if you need to download files every time the script is run.
autoDelete = True
# Set to True if you need to download server.
# Sometimes a version doesn't have a server.
# The way out is to either wrap it in try except, call the server download, or put False here.
downloadServer = False
# Launch username var
username = 'Player'
