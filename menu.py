import adventurelib as adv
from colorama import Fore as col
import os, time
from rooms import room1

def cls():
    os.system('cls')

class Menu:
    def __init__(self, current_room: int):
        self.current_room = current_room
        self.menu_active = True
        
    @property
    def text():
        return f"{col.GREEN}Welcome to Forest Escape!\nMain Menu Commands:" \
        f"\n- Play\n- Credits\n- Exit\n\n" \
        f"Please choose an option from the list above.{col.RESET}"
    
    @adv.when('play')
    def play(self):
        if self.menu_active is False:
            print(col.RED, "'play' is only available in the menu!", col.RESET)
            return
        cls()
        with open('assets/prologue.txt', 'r') as f:
            text = f.read().split('\n\n')
        for txt in text:
            print("\n", txt)
            time.sleep(3)
        input(f"\n{col.BLUE}Press ENTER to begin.{col.RESET}\n")
        cls()
        self.menu_active = False
        room1()

    @adv.when('credits')
    @adv.when('creds')
    def credits(self):
        if self.menu_active is False:
            print(col.RED, "'credits' is only available in the menu!",
                  col.RESET)
            return
        print(
            col.GREEN,
            "Forest Escape was designed and developed by:",
            "\n- Zack Hickson - 30237284\n- Thomas Long - 30235093",
            col.RESET
        )
        input(f"\n{col.BLUE}Press ENTER to continue.{col.RESET}")
        cls()
        print(self.text)

    @adv.when('exit game')
    @adv.when('exit')
    def exit_game(self):
        if self.menu_active is False:
            print(col.RED, "'exit' is only available in the menu!", col.RESET)
            return
        print(col.RED, "Closing game...", col.RESET)
        time.sleep(2)
        exit()

    def no_command_matches(self, command: str):
        print(f"{col.RED}'{command}' is not a valid menu command.{col.RESET}")

    def start(self):
        cls()
        print(self.text)
        adv.no_command_matches = no_command_matches
        adv.start(help=False)