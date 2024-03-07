import random
import os
def clear():  
    os.system('cls' if os.name == 'nt' else 'clear')
from art import logo
from art import vs
from game_data import data

game_end = False
score = 0
correct = ""

while not game_end:
    which_data_a = random.randint(0,49)
    print(f"Compare A: \n{data[which_data_a]['name']}, a {data[which_data_a]['description']}, from {data[which_data_a]['country']}.")
    print(data[which_data_a]['follower_count'])
    print(vs)
    which_data_b = random.randint(0,49)
    print(f"Compare B: \n{data[which_data_b]['name']}, a {data[which_data_b]['description']}, from {data[which_data_b]['country']}")
    print(data[which_data_b]['follower_count'])
    answer = input("Who has more followers? Type 'A' or 'B':").upper()

    if int(data[which_data_a]['follower_count']) > int(data[which_data_b]['follower_count']):
        correct = "A"
    else:
        correct = "B"
    
    if answer == correct:
        score +=1
        print(f"\nYou're right! Current score: {score}.\n")
    else:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
        game_end = True
