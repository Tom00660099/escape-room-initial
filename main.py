if __name__ == "__main__":
    from setup import setup_checks
    setup_checks()

import adventurelib as adv
from menu import Menu

if __name__ == "__main__":
    menu = Menu(0)
    menu.start()