if __name__ == "__main__":
    from setup import setup_checks
    setup_checks()

import adventurelib as adv
from colorama import Fore
import os, time
import funcs
from rooms import *

menu_active = True

game_data = dict()

def display_menu():
    print(
        Fore.GREEN,
        "Welcome to Forest Escape!\nMain Menu Commands:\n- Play\n"
        "- Credits\n- Exit\n\nPlease choose an option from the list above.", # retard
        Fore.RESET
    )
    

@adv.when('play')
def play():
    if menu_active is False:
        print(Fore.RED, "'play' is only available in the menu!", Fore.RESET)
        return
    funcs.cls()
    with open('assets/prologue.txt', 'r') as f:
        text = f.read().split('\n\n')
    for txt in text:
        print("\n", txt)
        time.sleep(3)

    room1()

@adv.when('credits')
@adv.when('creds')
def credits():
    print(
        Fore.GREEN,
        "Forest Escape was designed and developed by:\n- Zack Hickson - 30237284\nThomas Long - 30235093", # retard
        Fore.RESET
    )
    input(f"\n{Fore.BLUE}Press ENTER to continue.{Fore.RESET}\n")
    os.system('cls')
    display_menu()

@adv.when('exit game')
@adv.when('exit')
def exit_game():
    print(fore.RED, "Closing game...", Fore.RESET)
    time.sleep(3)
    exit()

def no_command_matches(command: str):
    print(f"{Fore.RED}'{command}' is not a valid menu command.{Fore.RESET}")

def start():
    display_menu()
    adv.no_command_matches = no_command_matches
    adv.start(help=False)

if __name__ == "__main__":
    start()