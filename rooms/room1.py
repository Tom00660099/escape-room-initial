from adventurelib import *
from random import choice
from colorama import Fore


Room.add_direction('north east', 'south west')
Room.add_direction('north west', 'south east')

prologue = Room("""  """)

current_room = prologue
Room.can_start = False

entrance = Room(""" 
This must be an entrance or something
Aye the rooms chilly Fam.
Bare Dark and that aswell,
There's like 8 doors about, one of em must be open
((Type a Direction to choose a door))
""")

prologue.can_start = True

@when('start')
def enter_entrance():
    global current_room
    if current_room.can_start is False:
        print(f"{Fore.RED}'start' is not a valid command.{Fore.RESET}")
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
        print("aye i found the exit fam")
    else :
        print("Not this one bro")



start()