from art import logo

import random
CORRECT_NUM = random.randint(1,100)

print ("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {CORRECT_NUM}")

mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
if mode == "hard":
    attempt = 5
else:
    attempt = 10

def game():
    global attempt
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess_num = int(input("Make a guess: "))
        attempt -=1
        if guess_num >CORRECT_NUM:
            print("Too high.")
        elif guess_num == CORRECT_NUM:
            print(f"You got it! The answer was {CORRECT_NUM}.")
        elif guess_num <CORRECT_NUM:
            print("Too low.")
    if attempt ==0:
        print("You've run out of guesses, you lose.")
game()