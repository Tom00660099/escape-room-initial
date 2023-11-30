import os, platform, time

def setup_checks():
    try:
        import adventurelib, colorama
    except ImportError:
        print("Installing requirements... Please wait.")
        if platform.system() == 'Linux':
            os.system('python3 -m pip install adventurelib colorama')
            os.system('clear')
        else:
            os.system('python -m pip install adventurelib colorama')
            os.system('cls')
    try:
        import adventurelib, colorama
    except ImportError:
        print("I failed to install requirements. Please try again.")
        time.sleep(5)
        exit()