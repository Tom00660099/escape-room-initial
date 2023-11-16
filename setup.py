import os, platform, time

def setup_checks():
    try:
        import adventurelib
    except ImportError:
        print("Installing requirements... Please wait.")
        if platform.system() == 'Linux':
            os.system('python3 -m pip install adventurelib')
            os.system('clear')
        else:
            os.system('python -m pip install adventurelib')
            os.system('cls')
    try:
        import adventurelib
    except ImportError:
        print("I failed to install requirements. Please try again.")
        time.sleep(5)
        exit()