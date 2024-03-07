# 我為何不能將『num1 = input("What's the first number?:" )』放在def 之外呢？
# 以及 counti = True 為何不能放在def 之外呢？

from art import logo
import os
def clear():  
    os.system('cls' if os.name == 'nt' else 'clear')

def calc():
    print(logo)
    conti = True
    num1 = input("What's the first number?:" )
    while conti:
        opera = input("+\n-\n*\n/\nPick an operation: ")
        num2 = input("What's the next number?: ")
        if opera == "+":
            counted = int(num1) + int(num2)
        elif opera == "-":
            counted = int(num1) - int(num2)
        elif opera == "*":
            counted = int(num1) * int(num2)
        elif opera == "/":
            counted = int(num1) / int(num2)
        else:
            return print("Undefine operation, please try again.")
        
        print(f"{num1} {opera} {num2} = {counted}")
        conti = input(f"Type 'y' to continue calculating with {counted}, or type 'n' to start a new calculation: ")
        if conti == "y":
            conti = True
            num1 = counted
        else:
            conti = False
            clear()
            calc()
calc()

