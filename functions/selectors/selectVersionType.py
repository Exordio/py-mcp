def selectVersionType(vi):
    versions = []
    versionsNumbs = []
    print('| Select the versioned branch to download (You can specify it with a number) |')
    print('1. Release\n2. Snapshot\n3. old_beta\n4. old_alpha')
    typeSelected = False
    while not typeSelected:
        versionType = input(' : ')
        if versionType == '1':
            versionType = 'release'
            typeSelected = True
        elif versionType == '2':
            versionType = 'snapshot'
            typeSelected = True
        elif versionType == '3':
            versionType = 'old_beta'
            typeSelected = True
        elif versionType == '4':
            versionType = 'old_alpha'
            typeSelected = True
        else:
            print('| Invalid value entered, please re-enter |')

    for i in vi['versions']:
        if i['type'] == versionType:
            versions.append(i)
            versionsNumbs.append(i['id'])

    return versions, versionsNumbs, versionType
