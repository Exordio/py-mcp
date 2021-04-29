from config.config import constants, autoDelete, autoRun
from functions.meta.createAutorunScript import runClient
from functions.meta.runBuilder import build

import shutil
import time
import os


def main():
    print('|  Python minecraft client generator 1.1  |\n')

    if os.path.exists(constants['package']['outputPath']):
        if autoDelete:
            print('Removing an old client... Three seconds to save the house...')
            time.sleep(3)
            print('Goodbye home!')
            shutil.rmtree('output')
        else:
            print(
                "The client directory already exists."
                "The client will be launched without downloading (if enabled in the config)."
                "We give three seconds to think..."
            )
            time.sleep(1)
            if autoRun:
                runClient()
            return
    build()


if __name__ == '__main__':
    main()
