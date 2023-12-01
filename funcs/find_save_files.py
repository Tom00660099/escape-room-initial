import os, json, typing

def findSaveFileNames() -> typing.List[str]:
    files = list()
    for item in os.listdir('save_files/'):
        if item.endswith('.json'):
            files.append(item.removesuffix('.json'))
    return files