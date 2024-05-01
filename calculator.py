from functions import *

orange_ascii_art = r"""
   ____    _    _     ____ ___  _        _  _____ ___  ____  
  / ___|  / \  | |   / ___/ _ \| |      / \|_   _/ _ \|  _ \ 
 | |     / _ \ | |  | |  | | | | |     / _ \ | || | | | |_) |
 | |___ / ___ \| |__| |__| |_| | |___ / ___ \| || |_| |  _ < 
  \____/_/   \_\_____\____\___/|_____/_/   \_\_| \___/|_| \_\
  
"""

orange_ascii_art = "\033[38;5;208m" + orange_ascii_art + "\033[0m"

print(orange_ascii_art)

while True:
    print("What do you want to do?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("Enter Q to Exit")

    choice = input("Enter your choice: ")

    if choice.lower() == 'q':
        break
    elif choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the number 1: "))
        num2 = float(input("Enter the number 2: "))
        
        if choice == '1':
            addition(num1, num2)
        elif choice == '2':
            subtraction(num1, num2)
        elif choice == '3':
            multiplication(num1, num2)
        elif choice == '4':
            division(num1, num2)
    else:
        print("Invalid choice!")
        continue

print("\n")
