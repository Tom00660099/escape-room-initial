if __name__ == "__main__":
    from setup import setup_checks
    setup_checks()  # ensure imports

import adventurelib as adv  # adventurelib - used for game commands
from colorama import Fore  # used for colours
import os, time
import funcs

def display_menu():
    print(
        Fore.GREEN,
        """
Welcome to Forest Escape!
Main Menu Commands:
    New Game
    Load Game
    Credits
    Exit Game

Please choose an option from the list above.
        """,
        Fore.RESET
    )

@adv.when('new game')
@adv.when('new')
def new_game():
    while True:
        name = input("Please enter a name for your save file:\n>>> ")
        if os.exists(f'save_files/{name}.json') is True:
            print("That name is already used. Please enter a new name.")
        else:
            break
    funcs.createSaveFile(name)

@adv.when('load game')
@adv.when('load')
def load_game():
    pass  # TODO

@adv.when('credits')
def credits():
    print(
        Fore.GREEN,
        """
Forest Escape was designed and developed by:
    Zack Hickson - 30237284
    Thomas Long - 30235093
    Jacob Hill - 30235348
        """,
        Fore.RESET
    )
    display_menu()

@adv.when('exit game')
@adv.when('exit')
def exit_game():
    print(Fore.RED, "Closing game...", Fore.RESET)
    time.sleep(4)
    exit()

def no_command_matches(command: str):
    print(f"{Fore.RED}'{command}' is not a valid menu command.{Fore.RESET}")

def start():
    display_menu()
    adv.no_command_matches = no_command_matches
    adv.start()

if __name__ == "__main__":
    start()