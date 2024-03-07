## name a var into global by using "UPPERCASE"
## it's not allow to modified the var






from art import logo

import random
CORRECT_NUM = random.randint(1,100)

print ("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {CORRECT_NUM}")

mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
if mode == "hard":
    ATTEMPT = 5
else:
    ATTEMPT = 10

    

def game():
    while ATTEMPT > 0:
        print(f"You have {ATTEMPT} attempts remaining to guess the number.")
        guess_num = int(input("Make a guess: "))
        ATTEMPT -=1
        if guess_num >CORRECT_NUM:
            print("Too high.")
        elif guess_num == CORRECT_NUM:
            print(f"You got it! The answer was {CORRECT_NUM}.")
        elif guess_num <CORRECT_NUM:
            print("Too low.")
    if ATTEMPT ==0:
        print("You've run out of guesses, you lose.")
game()