import os, typing, json

def getSaveFile(name: str) -> typing.Dict[str, typing.Any]:
    if os.path.exists(f'save_files/{name}.json') is False:
        raise ValueError("Incorrect save file name.")
    with open(f'save_files/{name}.json', 'r') as f:
        data = json.load(f)
    return data