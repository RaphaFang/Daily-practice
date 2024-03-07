rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
pic = [rock, paper, scissors]
result = ["It's a draw", "You lose", "You win"]
import random
player = input("What do you choose?\nType 0 for Rock,1 for Paper or 2 for Scissors.")
pc = random.randint(0, 2)

if int(player) > 2:
    print("You typed an inavalid number, you lose!")
else:
    print(pic[int(player)])
    print("Computer chose:")
    print(pic[pc])
    pc = str(pc)
    combin = player+str(pc)

    if player==pc: # draw
        print(result[0]) 
    elif combin == "01" or combin == "12" or combin == "20": # You lose
        print(result[1])
    else:
        combin == "02" or combin =="10" or combin =="21" # You win
        print(result[2])