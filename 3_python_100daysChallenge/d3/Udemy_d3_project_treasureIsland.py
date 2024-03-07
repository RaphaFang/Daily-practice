print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

left_or_right = input("Where would you like to go?\nLeft or right?").lower()
if left_or_right == "left":
    swim_or_wait = input("There is a lake infront of you. In the middle of the lake, there\'s a island.\nSwim or wait?").lower()
    if swim_or_wait == "wait":
        which_door = input("You\'re now on the island. There\'s a house with 3 doors.\nOne red, one yellow and one blue.\nWhich door?").lower()
        if which_door == "red":
            print("Burned by fire.\nGame Over.")
        elif which_door == "yellow":
            print("You Win!")
        elif which_door == "blue":
            print("Eaten by beasts.\nGame Over.")
        else:
            print("Game Over")
    else:
        print("Attacked by trout.\nGame Over")
else:
  print("Fall into a hole.\nGame Over.")
## when you want to type you're and keep the( ' ), do ("you\'re")