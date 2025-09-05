import os
import sys
import time

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def file_shredder():
    clear
    for i in range(5):
        print("\rShredding the File", end="", flush=True)
        sys.stdout.flush()
        time.sleep(1)
    clear()
    path = input("Drag and Drop File to shred here >> ")
    try:
        if not os.path.exists(path):
            print("File Not Found")
            file_shredder()
        print("\nFile Found...")
        for i in range(5):
            print(f"Shredding the File" + "." * (i + 1), end="\r", flush=True)
            time.sleep(1)
        print()
    except Exception as e:
        print(f"Error >> {e}")

if __name__ == "__main__":
    file_shredder()
