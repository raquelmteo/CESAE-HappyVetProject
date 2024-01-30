"""
THIS PROGRAM WAS CREATED BY
- RAQUEL DE MELO TEÓFILO
- MARIA LUISA FREITAS DE LUCENA
"""

import os

# Prints lines
def line(size=42):
    return "-" * size

# Prints centralized menu with lines 
def printMenuHeader(txt):
    print(line()) 
    print(txt.center(40))
    print(line())

# Prints menu 
def displayMenu(menu, title):
    printMenuHeader(title)
    i = 1
    for item in menu:
        print(f"({i}) {item}")
        i += 1
    print(line())

# Gets valid integer input from user
def getIntegerInput(input_msg, min_val, max_val):
    while(True):
        try:
            userInput = int(input(input_msg))
        except (ValueError, TypeError):
            print("ERROR! Insert a valid option")
        else: 
            if userInput < min_val or userInput > max_val:
                print("ERROR! Option doesn't exist")
            else:
                return userInput

# Clears cli
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear') 
