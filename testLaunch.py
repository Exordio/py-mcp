# -*- coding: utf-8 -*-
import os
# java -jar client.jar --username Exord --gameDir . --assetsDir assets1.12.2 --assetIndex 1.12 --uuid hui --accessToken her --userType admin --versionType 1.12.2 -cp output\

arguments = []

arguments.append('java')
arguments.append('-Djava.library.path=natives')
arguments.append('-XX:HeapDumpPath=ThisTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump')

classPath = []

_, _, filenames = next(os.walk('libraries'))

for i in range(len(filenames)):
    filenames[i] = f'libraries/{filenames[i]}'

classSex = ';'.join(filenames)

arguments.append(f'-cp client.jar;{classSex}')
arguments.append(f'net.minecraft.client.main.Main')

arguments.append('--username Exord')
arguments.append('--gameDir .')
arguments.append('--assetsDir assets1.12.2')
arguments.append('--assetIndex 1.12')
arguments.append('--uuid hui')
arguments.append('--accessToken her')
arguments.append('--userType --mojang')
arguments.append('--versionType --release')
arguments.append('--version 1.12.2')


launchStr = f''' '''.join(arguments)
print(launchStr)

launch = os.system(launchStr)
print(f'{launch}')