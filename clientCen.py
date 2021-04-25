import os
import json


def readJson(path):
    with open(path) as json_file:
        data = json.load(json_file)

    print(data)


def listAssetsDir(path):
    listAssetsJsons = os.listdir(path)

    assetsDict = {}
    for i in range(len(listAssetsJsons)):
        assetsDict = {i: listAssetsJsons[i]}
        print(f'{i} - {listAssetsJsons[i]}')

    return assetsDict


def selectAssets():
    assetsPath = f'''{os.path.expanduser("~")}/AppData/Roaming/.minecraft/assets/indexes'''
    print('| Шаг 1. Выбор asset. Необходимо выбрать нужный ассет из меню ниже. |\n')
    toSelectAssetsDict = listAssetsDir(assetsPath)

    correct = False
    while not correct:
        selectedAssetNum = input(": ")
        try:
            print(toSelectAssetsDict[int(selectedAssetNum)])
            correct = True
        except KeyError:
            print('| Неверный номер меню, повторите ввод |')


if __name__ == '__main__':
    print('|  GreatRay client generator 0.1 |')
    selectAssets()

