import os
import subprocess
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_game(filename):
    try:
        subprocess.run([sys.executable, filename],
                       cwd="src/gamesbyexample")
    except FileNotFoundError:
        print("Game file not found!")
        input("Press Enter to continue...")

while True:
    clear()
    print("===================================")
    print("   COGNIFYZ INTERNSHIP GAME HUB   ")
    print("===================================")
    print("1. Four In A Row")
    print("2. Maze Runner")
    print("3. Snail Race")
    print("4. Exit")
    print("===================================")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        run_game("fourinarow.py")
    elif choice == "2":
        run_game("mazerunner2d.py")
    elif choice == "3":
        run_game("snailrace.py")
    elif choice == "4":
        print("Exiting Game Hub...")
        break
    else:
        print("Invalid choice!")
        input("Press Enter to continue...")
