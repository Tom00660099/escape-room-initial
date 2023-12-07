if __name__ == "__main__":
    from setup import setup_checks
    setup_checks()  # ensure imports

import adventurelib as adv  # adventurelib - used for game commands
from colorama import Fore  # used for colours
import os, time
import funcs

game_data = dict()

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
        if name.lower() == "cancel":
            os.system('cls')
            display_menu()
            return
        if os.path.exists(f'save_files/{name}.json') is True:
            print(f"{Fore.RED}That name is already used. Please enter a new name.{Fore.RESET}")
        else:
            break
    funcs.createSaveFile(name)
    game_data = funcs.getSaveFile(name)
    os.system('cls')
    print(f"{Fore.GREEN}Save file created!{Fore.RESET}")
    # send prologue
    with open('assets/prologue.txt', 'r') as f:
        text = f.read().split('\n\n')
    for txt in text:
        print(txt)
        time.sleep(1.5)
    
    # TODO: start room1


@adv.when('load game')
@adv.when('load')
def load_game():
    file_names = funcs.findSaveFileNames()
    text = f"{Fore.RESET}Please enter a number from the list below.\n"
    for i in range(1, len(file_names)+1):
        text += f"{Fore.GREEN}{i}{Fore.RESET} - {Fore.BLUE}{file_names[i-1]}{Fore.RESET}"
    while True:
        os.system('cls')
        print(text)
        num = input(">>> ")
        if num.lower() == "cancel":
            os.system('cls')
            display_menu()
            return
        if num.isdigit() is False:
            print(f"{Fore.RED}Incorrect input!{Fore.RESET}")
        else:
            try:
                num = int(num)
            except:
                print(f"{Fore.RED}Incorrect input!{Fore.RESET}")
            else:
                if num <= len(file_names):
                    break
                else:
                    print(f"{Fore.RED}Incorrect input!{Fore.RESET}")
        time.sleep(2)
    name = file_names[num - 1]
    try:
        game_data = funcs.getSaveFile(name)
    except:
        print(f"{Fore.RED}Save file doesn't exist anymore!{Fore.RESET}")
        input(f"{Fore.RED}\nPress ENTER to continue.{Fore.RESET}")
        os.system('cls')
        display_menu()
        return
    

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
    input(f"\n{Fore.BLUE}Press ENTER to continue.{Fore.RESET}\n")
    os.system('cls')
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