import sys
import os

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def setup():
    try:
        if sys.platform.startswith("win"):
            clear()
            print("Installing the python modules required for the Zenith Tool")
            os.system("python -m pip install --upgrade pip")
            os.system("python -m pip install -r requirements.txt")
            os.system("python main.py")
        elif sys.platform.startswith("linux"):
            clear()
            print("Installing the python modules required for the Zenith Tool")
            os.system("python3 -m pip install --upgrade pip")
            os.system("python3 -m pip install -r requirements.txt")
            os.system("python3 main.py")
    except Exception as e:
        input(f"Error >> {e}")

if __name__ == "__main__":
    setup()