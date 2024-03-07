import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for n in range(0, len(chosen_word)):
    display.append("_")

guess_times = 0
while not guess_times == int(len(chosen_word)):
    guess = input("Guess a letter: ").lower()
    for block in range(len(chosen_word)):
        letter = chosen_word[block]
        print(f"Current position: {block}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[block] = letter
            guess_times +=1





print(display)

## i can't make this immidiately, need more practice...
## you can set the var(int or str) in the "for" function,
    ## just base on if there is a "range" function after it or not.
    ## e.g. 
    # fruits = ["a", "b"]
    # for a in fruits:
    #     print(fruit)
    ## in this situation, "a" is a "str", 
    ## but the upper paragraphe the "block" is "int".