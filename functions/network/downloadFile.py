from functions.network.request import request


def downloadFile(url, filename, dist, count=0):
    with open(f'''{dist}/{filename}''', 'wb') as file:
        file.write(request(url, content=True))

    print(f'''| Загружен {filename} : Осталось {count} файлов |''')
