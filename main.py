def display_menu() -> list[str]:
    print(
        """
Welcome to Forest Escape!
Below you will see the main menu.

    1 - New Game
    2 - Load Game
    3 - Exit Game

Please choose a number from the list above.
        """
    )
    return ["1", "2", "3"]

def menuinput():
    while True:
        allowed_options = display_menu()
        option = input("> ")
        if option not in allowed_options:
            print("Invalid option! Please try again.")
        else:
            break

    option = int(option)
    if option == 1:
        pass  # TODO
    elif option == 2:
        pass  # TODO
    else:
        exit()  # ? maybe add "thanks for playing..." message and time sleep for 5 seconds before exit

if __name__ == "__main__":
    menuinput()