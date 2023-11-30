if __name__ == "__main__":
    from setup import setup_checks
    setup_checks()

import adventurelib as adv
import colorama
import os, time

def display_menu():
    print(
        """
Welcome to Forest Escape!
Main Menu:
    New Game
    Load Game
    Credits
    Exit Game

Please choose an option from the list above.
        """
    )

@adv.when('new game')
@adv.when('new')
def new_game():
    pass  # TODO

@adv.when('load game')
@adv.when('load')
def load_game():
    pass  # TODO

@adv.when('credits')
def credits():
    print(
        """
Forest Escape was designed and developed by:
    Zack Hickson
    Thomas Long
    Jacob Hill
        """
    )

@adv.when('exit game')
@adv.when('exit')
def exit_game():
    print("Closing game...")
    time.sleep(4)
    exit()

def start():
    adv.start()