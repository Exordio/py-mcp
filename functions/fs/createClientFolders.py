import os

from config.config import constants


def createClientFolders(vd):
    # Create a folder for the output of the script
    try:
        os.mkdir(constants['package']['outputPath'])
    except FileExistsError:
        pass

    # Create a folder for libraries
    try:
        os.mkdir(f'''{constants['package']['outputPath']}/{constants['package']['librariesDir']}''')
    except FileExistsError:
        pass

    # Create a folder for native.
    try:
        os.mkdir(f'''{constants['package']['outputPath']}/{constants['package']['nativesDir']}''')
    except FileExistsError:
        pass

    # Create a folder for assets
    try:
        os.makedirs(
            f'''{constants['package']['outputPath']}/{constants['package']['assetsDir']}/indexes''')
    except FileExistsError:
        pass