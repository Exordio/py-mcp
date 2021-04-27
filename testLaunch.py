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

classSex = ';'.join(filenames)

arguments.append(f'-cp output/client.jar;{classSex}')
arguments.append(f'net.minecraft.client.main.Main')

arguments.append('--username Exord')
arguments.append('--gameDir output/')
arguments.append('--assetsDir output/assets1.16.5')
arguments.append('--assetIndex 1.16')
arguments.append('--uuid hui')
arguments.append('--accessToken her')
arguments.append('--userType --mojang')
arguments.append('--versionType --release')
arguments.append('--version 1.16.5')


launchStr = f''' '''.join(arguments)
print(launchStr)

launch = os.system(launchStr)
print(f'{launch}')