from adventurelib import *
from random import choice, shuffle
from colorama import Fore

Room.add_direction('north east', 'south west')
Room.add_direction('north west', 'south east')

prologue = Room(""" """)

current_room = proglogue
Room.can_start = False

entrance = Room(
    """
This must be an entrance or something.
Aye the rooms chilly Fam.
Bare Dark and that aswell,
There's like 8 doors about, one of em must be open.
((Type a Direction to choose a door. Example: north east))
    """
)

prologue.can_start = True

@when('start')
def enter_entrance():
    global current_room
    if current_room.can_start is False:
        print(f"{Fore.RED}'start' can only be used in the menu.{Fore.RESET}")
        return
    current_room = entrance
    print(current_room)

directions = ["north", "north east", "east", "south east", "south", "south west", "west", "north west"]
correct_door = choice(directions)
fail_responses_list = [
    "Oi, fam, you must be joking! That door's proper locked up. It ain't just gonna swing open for you like it's your front yard. Check the signs, bruv, and find the real escape route.",
    "Hold on, hold on! You thought that door was gonna magically open? Nah, fam, it's locked up tight. You gotta use your head, not just try any old door, you get me?",
    "Oi, what you playin' at? That door's locked like Fort Knox. You can't just stroll through any old entrance, blud. Look for the right one, and maybe you'll actually get out of here.",
    "Bruh, did you miss the memo? Wrong door means locked door. It's not a game of luck, it's a game of brains. Sort it out and find the one that ain't bolted shut.",
    "You've got the wrong door, and guess what? It's locked, my guy. Ain't no luck in that choice. Better luck next time, and try not to pick the doors that don't budge.",
    "Hold up, hold up! That door's as locked as a safe. You need to be smarter, fam. The right door ain't just gonna open for anyone. Look before you leap, innit?",
    "Not this one bro."
]
fail_responses = {}
incorrect_directions = directions.copy()
incorrect_directions.remove(correct_door)
shuffle(incorrect_directions)
for i in range(7):
    fail_responses[incorrect_directions[i]] = fail_responses_list[i]


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
    if direction == correct_door:
        print("aye i found the exit fam")
    else:
        print(fail_responses[direction])


def _start():
    start()