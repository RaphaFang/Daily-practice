import random
random_int = random.randint(1, 10)
print(random_int)

random_float = random.random()
print(random_float)

## the way to generate a random float from 0~5?
## random_float*5 would help, the range for random_float, is 0.000...1~4.9999...

# 1.____________________________________________________________
import random
random_int = random.randint(0,1)

if random_int ==0:
  print("Tails")
else:
  print("Heads")

# 2.____________________________________________________________
## just_a_test[-1], you'll get the last picce of data in the list.
names_string = input()  # detect the str
names = names_string.split(", ")  # build the list
the_len = len(names)
import random
random_int = random.randint(1, the_len)
random_int -= 1
unlucky_guy = names[random_int]
print(f"{unlucky_guy} is going to buy the meal today!")
# the e.g. for name list input, Angela, Ben, Jenny, Michael, Chloe

# 3.____________________________________________________________
line1 = ["⬜","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

letter = position [0].lower()
number = int(position [1])
front_block = 0
back_block = 0

if letter == "a":
  front_block = 0
elif letter == "b":
  front_block = 1
else:
  letter == "c"
  front_block = 2
if number -1 == 0:
  back_block =0
elif number -1 == 1:
  back_block =1
else:
  number -1 == 2
  back_block =2

map[back_block][front_block] = 'X'
print(map[0])
print(map[1])
print(map[2])
## type X[0][0],not X[[0][0]] either X[[0],[0]] 
## if you want to call the first array's first array