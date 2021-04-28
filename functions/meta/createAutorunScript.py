from config.config import platform, autoRun
from datetime import datetime
from zipfile import ZipFile
from config.config import constants

import shutil
import os

separator = ';' if platform == 'windows' else ':'


def createAutorunScript(versionIndex, assetIndex, versionType, magicImpotantMushrooms):
    with ZipFile(f'''{constants['package']['outputPath']}/client.jar''', 'r') as zipObj:
        zipObj.extractall(f'''temp''')

    with open('temp/META-INF/MANIFEST.MF', 'r') as mainClassManifest:
        for i in mainClassManifest.readlines():
            if i.startswith('Main-Class:'):
                mainClassName = i.strip().split(' ')[-1]
    if mainClassName == 'net.minecraft.client.Main':
        mainClassName = 'net.minecraft.client.main.Main'
    shutil.rmtree('temp')

    print(f'\n| {datetime.now().time()} Создаем скрипт запуска |')

    runScript = '''import os
arguments = []
arguments.append(f\'\'\'set APPDATA={os.path.abspath('data')}&&\'\'\')\n'''
    runScript += '''arguments.append('java')
arguments.append('-Duser.home="' + os.path.abspath('data') + '"')
arguments.append('-Djava.library.path="' + os.path.abspath('natives') + '"')
arguments.append('-XX:HeapDumpPath=ThisTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump')
classPath = []
_, _, filenames = next(os.walk('libraries'))
for i in range(len(filenames)):
    filenames[i] = f'libraries/{filenames[i]}'
'''
    runScript += f'''classPathFiles = '{separator}'.join(filenames)\n'''
    runScript += f'''arguments.append(f\'-cp client.jar{separator}''' + '''{classPathFiles}\')\n'''
    runScript += f'''arguments.append('{mainClassName}')
arguments.append('{'--username username' if not magicImpotantMushrooms else 'username null'}')\n'''
    runScript += f'''arguments.append('--gameDir "' + os.path.abspath('.') + '"')
arguments.append('--workDir "' + os.path.abspath('.') + '"')
arguments.append('--assetsDir "' + os.path.abspath('assets') + '"')
arguments.append('--assetIndex {assetIndex}')
arguments.append('--uuid 0')
arguments.append('--accessToken 0')
arguments.append('--userType --mojang')
arguments.append('--versionType --{versionType}')
arguments.append('--version {versionIndex}')
'''
    runScript += '''arguments.append('--userProperties {}')
launchStr = f\'\'\' \'\'\'.join(arguments)
print(launchStr)
launch = os.system(launchStr)
print(f'{launch}')

'''
    print(f'| {datetime.now().time()} Скрипт запуска создан! |\n')

    with open(f"{constants['package']['outputPath']}/start.py", 'w') as startScript:
        startScript.write(runScript)

    if autoRun:
        run()


def run():
    cur_dir = os.path.abspath(".")
    os.chdir(f"{cur_dir}/{constants['package']['outputPath']}")
    if platform == 'windows':
        os.system(f'\"{cur_dir}/venv/scripts/python\" start.py')
    else:
        os.system(f'\"{cur_dir}/venv/bin/python\" start.py')
