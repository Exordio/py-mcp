import os
import sys
import json
import shutil


assetsIndexesPath = f'''{os.path.expanduser("~")}/AppData/Roaming/.minecraft/assets/indexes/'''
assetsObjectsPath = f'''{os.path.expanduser("~")}/AppData/Roaming/.minecraft/assets/objects/'''
genFolder = 'Client'


def listAssetsDir(path):
    listAssetsJsons = os.listdir(path)

    assetsDict = {}
    for i in range(len(listAssetsJsons)):
        assetsDict = {i: listAssetsJsons[i]}
        print(f'{i} - {listAssetsJsons[i]}')
    return assetsDict


def selectAssets():
    print('| Шаг 1. Выбор asset. Необходимо выбрать нужный ассет из меню ниже. |\n')
    toSelectAssetsDict = listAssetsDir(assetsIndexesPath)
    correct = False
    while not correct:
        selectedAssetNum = input(": ")
        try:
            print(toSelectAssetsDict[int(selectedAssetNum)])
            correct = True
        except KeyError:
            print('| Неверный номер меню, повторите ввод |')

    # Создаём директорию для ассета
    try:
        os.mkdir(f'''{genFolder}/asset{toSelectAssetsDict[int(selectedAssetNum)].replace('.json', '')}''')
    except FileExistsError:
        print('| Папка для выбранного ассета уже существует, пропускаем создание. |')

    return toSelectAssetsDict[int(selectedAssetNum)]


def readJson(path):
    with open(path) as json_file:
        data = json.load(json_file)
    return data


def createAssetFsStructure(sa):
    try:
        os.mkdir(f'''{genFolder}/asset{sa.replace('.json', '')}/indexes''')
    except FileExistsError:
        print("| При создании папки индексов ассетов, было обнаружено что папка уже существует, пропускаем |")
    try:
        os.mkdir(f'''{genFolder}/asset{sa.replace('.json', '')}/objects''')
    except FileExistsError:
        print("| При создании папки объектов ассетов, было обнаружено что папка уже существует, пропускаем |")


def createAssetObjectSubFolder(folder, sa):
    try:
        os.mkdir(f'''{genFolder}/asset{sa.replace('.json', '')}/objects/{folder}''')
    except FileExistsError:
        pass


def copyAssetObj(assetHash, sa):
    originalAssetObjPath = f'''{assetsObjectsPath}{assetHash[0:2]}/{assetHash}'''
    targetAssetObjPath = f'''{genFolder}/asset{sa.replace('.json', '')}/objects/{assetHash[0:2]}/'''
    sys.stdout.write(f'''\r| Копируем {assetHash} |''')
    sys.stdout.flush()

    shutil.copy(originalAssetObjPath, targetAssetObjPath)


def copyAssetIndexesFile(sa):
    print(f'\n| Копируем {sa} |')
    originalAssetIndexPath = f'''{assetsIndexesPath}{sa}'''
    targetAssetIndexPath = f'''{genFolder}/asset{sa.replace('.json', '')}/indexes/'''
    shutil.copy(originalAssetIndexPath, targetAssetIndexPath)


def findNCopyAssets(assetIndex, sa):
    print('\n')
    for i in assetIndex['objects']:
        createAssetObjectSubFolder(assetIndex['objects'][i]['hash'][0:2], sa)
        copyAssetObj(assetIndex['objects'][i]['hash'], sa)

    copyAssetIndexesFile(sa)

    print('\n| Копирование assets завершено. |')


if __name__ == '__main__':
    print('|  GreatRay client generator 0.1 |')
    print('| Предварительно создаём новую папку для генерации клиента |')
    try:
        os.mkdir(genFolder)
    except FileExistsError:
        print('| Папка уже создана |')

    selectedAsset = selectAssets()
    assetsJsonObj = readJson(assetsIndexesPath + selectedAsset)
    createAssetFsStructure(selectedAsset)
    findNCopyAssets(assetsJsonObj, selectedAsset)

