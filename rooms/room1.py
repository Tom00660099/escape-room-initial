from adventurelib import *
from random import choice


Room.add_direction('north east', 'south west')
Room.add_direction('north west', 'south east')

prologue = Room("""  """)

current_room = prologue

entrance = Room(""" 
Aye the rooms chilly Fam.
Bare Dark and that aswell,
There's like 8 doors about, one of em must be open.
""")

Room.can_start = False
prologue.can_start = True

@when('start')
def enter_entrance():
    global current_room
    if current_room.can_start is False:
        print("how have you done this shit")
        return
    current_room = entrance
    print(current_room)


correct_door = choice(["north", "north east", "east", "south east", "south", "south west", "west", "north west"])

@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
@when('north east', direction='north east')
@when('north west', direction='north west')
@when('south east', direction='south east')
@when('south west', direction='south west')
def go(direction):
    global current_room
    if direction == correct_door :
        print("congrats")



start()