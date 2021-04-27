from config.config import platform, autoRun
from datetime import datetime

import os

separator = ';' if platform == 'windows' else ':'


def createAutorunScript(versionIndex, assetIndex, versionType):
    print(f'|\n {datetime.now().time()} Создаем скрипт запуска |')
    autoRun = '''import os
arguments = []
arguments.append('java')
arguments.append('-Djava.library.path=natives')
arguments.append('-XX:HeapDumpPath=ThisTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump')
classPath = []
_, _, filenames = next(os.walk('libraries'))
for i in range(len(filenames)):
    filenames[i] = f'libraries/{filenames[i]}'
    '''
    autoRun += f'''classPathFiles = '{separator}'.join(filenames)\n'''
    autoRun += f'''arguments.append(f'-cp client.jar{separator}''' + '''{classPathFiles}\')\n'''
    autoRun += f'''arguments.append(f'net.minecraft.client.main.Main')
arguments.append('--username Username')
arguments.append('--gameDir .')
arguments.append('--assetsDir assets{versionIndex}')
arguments.append('--assetIndex {assetIndex}')
arguments.append('--uuid 0')
arguments.append('--accessToken 0')
arguments.append('--userType --mojang')
arguments.append('--versionType --{versionType}')
arguments.append('--version {versionIndex}')
launchStr = f\'\'\' \'\'\'.join(arguments)
'''
    autoRun += '''print(launchStr)
launch = os.system(launchStr)
print(f'{launch}')

'''
    print(f'| {datetime.now().time()} Скрипт запуска создан! |')

    with open('output/start.py', 'w') as startScript:
        startScript.write(autoRun)

    if autoRun:
        os.system('venv/scripts/activate && python output/start.py')
