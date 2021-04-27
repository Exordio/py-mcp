def selectVersion(v, vn):
    print(vn)
    print('| Введите номер версии для сборки клиента |')
    finded = False
    while not finded:
        versionSelect = input(' : ')
        for i in vn:
            if i == versionSelect:
                print('| Версия найдена |')
                finded = True
                break
        if not finded:
            print('| Версия не найдена, повторите ввод. |')

    for i in v:
        if i['id'] == versionSelect:
            return i
