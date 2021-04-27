from config.config import platform, autoRun
from datetime import datetime
from zipfile import ZipFile

import shutil
import os

separator = ';' if platform == 'windows' else ':'


def createAutorunScript(versionIndex, assetIndex, versionType):
    with ZipFile(f'''output/client.jar''', 'r') as zipObj:
        zipObj.extractall(f'''temp''')

    with open('temp/META-INF/MANIFEST.MF', 'r') as mainClassManifest:
        for i in mainClassManifest.readlines():
            if i.startswith('Main-Class:'):
                mainClassName = i.strip().split(' ')[-1]
    shutil.rmtree('temp')

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
    autoRun += f'''classPathFiles = '{separator}'.join(filenames)\n
arguments.append(f'-cp client.jar{separator}''' + '''{classPathFiles}\')\n
arguments.append(f'{mainClassName}')
arguments.append('--username Username')
arguments.append('--gameDir .')
arguments.append('--assetsDir assets{versionIndex}')
arguments.append('--assetIndex {assetIndex}')
arguments.append('--uuid 0')
arguments.append('--accessToken 0')
arguments.append('--userType --mojang')
arguments.append('--versionType --{versionType}')
arguments.append('--version {versionIndex}')
'''
    autoRun += '''arguments.append('--userProperties {}')
launchStr = f\'\'\' \'\'\'.join(arguments)
print(launchStr)
launch = os.system(launchStr)
print(f'{launch}')

'''
    print(f'| {datetime.now().time()} Скрипт запуска создан! |')

    with open('output/start.py', 'w') as startScript:
        startScript.write(autoRun)

    if autoRun:
        cur_dir = os.path.abspath(".")
        os.chdir(f'{cur_dir}/output')
        if platform == 'windows':
            os.system(f'\"{cur_dir}/venv/scripts/python\" start.py')
        else:
            os.system(f'\"{cur_dir}/venv/bin/python\" start.py')
