def selectVersion(v, vn):
    print(vn)
    print('| Enter the version number for the client build |')
    finded = False
    while not finded:
        versionSelect = input(' : ')
        for i in vn:
            if i == versionSelect:
                print('| Version found |')
                finded = True
                break
        if not finded:
            print('| No version found, please re-enter. |')

    for i in v:
        if i['id'] == versionSelect:
            return i
