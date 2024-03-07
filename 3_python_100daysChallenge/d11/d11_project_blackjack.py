import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
computer_cards = []
another_card = "y"
def total_score_both():
    sum(your_cards)
    sum(computer_cards)


start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start == "y":
    your_cards.append(random.choice(cards))
    your_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

    

    total_score_both()
    print(logo)
    print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    while sum(your_cards)< 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card=="y":
            your_cards.append(random.choice(cards))
            print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    while sum(computer_cards)< 21:
        computer_cards.append(random.choice(cards))

    if sum(your_cards) > sum(computer_cards):
        print(f"Your cards: {your_cards}, current score: {sum(your_cards)}.\n    Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\nYou win 😃")
    elif sum(your_cards) == sum(computer_cards):
        print("draw")
    elif sum(your_cards) < sum(computer_cards):
        print(f"Your cards: {your_cards}, current score: {sum(your_cards)}.\n    Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\nYou lose 😤")
    
