# -*- coding: utf-8 -*-
import os

arguments = []

arguments.append('java')
arguments.append('-Djava.library.path=output1/natives')
arguments.append('-XX:HeapDumpPath=ThisTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump')

classPath = []

_, _, filenames = next(os.walk('output1/libraries'))

for i in range(len(filenames)):
    filenames[i] = f'output1/libraries/{filenames[i]}'

classPathFiles = ';'.join(filenames)

arguments.append(f'-cp output1/client.jar;{classPathFiles}')
arguments.append(f'net.minecraft.client.main.Main')

arguments.append('--username Exord')
arguments.append('--gameDir output1/')
arguments.append('--assetsDir output1/assets21w16a')
arguments.append('--assetIndex 1.17')
arguments.append('--uuid hui')
arguments.append('--accessToken her')
arguments.append('--userType --mojang')
arguments.append('--versionType --snapshot')
arguments.append('--version 21w16a')


launchStr = f''' '''.join(arguments)
print(launchStr)

launch = os.system(launchStr)
print(f'{launch}')