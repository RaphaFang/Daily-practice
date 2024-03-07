# from replit import clear
import os
def clear():  
    os.system('cls' if os.name == 'nt' else 'clear')

from art import logo
print(logo)
print("Welcome to the secret auction program.")

dict_for_all = {}
more_bidder = "yes"
while more_bidder == "yes":
    name = input("What is your name?\n")
    bid = int(input("What's your bid?\n$"))
    more_bidder = input("Are there any more bidders? Type 'yes' or 'no'\n")
    dict_for_all[name] = bid
    # clear() ---- without "clear()"

## print(dict_for_all)
## a check point

winner=["", 0]
biggist = 0
for n in dict_for_all:
    if dict_for_all[n] > biggist:
        biggist = dict_for_all[n]
        winner[0] = n
        winner[1] = biggist

print(f"The winner is {winner[0]} with a bid of ${winner[1]}.")