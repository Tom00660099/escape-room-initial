import json

standard_data = dict(
    current_room="Room1",
    inventory=[],
    rooms_visited=["Room1"],
    lastest_room_unlocked="Room1"
)

def createSaveFile(name: str):
    f = open(f'save_files/{name}.json')
    json.dump(standard_data, f)
    f.close()
    return True