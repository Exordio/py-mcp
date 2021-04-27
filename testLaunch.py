# -*- coding: utf-8 -*-
import os

arguments = []

arguments.append('java')
arguments.append('-Djava.library.path=output/natives')
arguments.append('-XX:HeapDumpPath=ThisTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump')

classPath = []

_, _, filenames = next(os.walk('output/libraries'))

for i in range(len(filenames)):
    filenames[i] = f'output/libraries/{filenames[i]}'

classPathFiles = ';'.join(filenames)

arguments.append(f'-cp output/client.jar;{classPathFiles}')
arguments.append(f'net.minecraft.client.main.Main')

arguments.append('--username Exord')
arguments.append('--gameDir output/')
arguments.append('--assetsDir output/assets1.12.2')
arguments.append('--assetIndex 1.12')
arguments.append('--uuid 0')
arguments.append('--accessToken 0')
arguments.append('--userType --mojang')
arguments.append('--versionType --release')
arguments.append('--version 1.12.2')


launchStr = f''' '''.join(arguments)
print(launchStr)

launch = os.system(launchStr)
print(f'{launch}')