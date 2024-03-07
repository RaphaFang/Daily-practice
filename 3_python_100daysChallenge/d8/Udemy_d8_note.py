# 1.____________________________________________________________
# def greet(name):
#     print=("what's your name?\n") 
#     print(f"Hello, {name}")
#     print(":)")
# greet("A")

## somethimg = 123
## parameter, is the name we give to the data.
## argument, is the data gonna pass through the function.
## 82.cg


# 2.____________________________________________________________
# def greet_with_2properties (name, location):
#     print(f"Hello, {name}")
#     print(f"what's it like in {location}?") 
#     print(":)")
# greet_with_2properties(location = "Taipei", name = "Rapha")


# 3.____________________________________________________________
import math

def paint_calc(height, width, cover):
  number_of_cans = (height * width) /cover
  number_of_cans = math.ceil(number_of_cans)
  print(f"You'll need {number_of_cans} cans of paint.")

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

## 


# 4.____________________________________________________________
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime == True:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")   
n = int(input()) 
prime_checker(number=n)

# >>>range(10)        # 从 0 开始到 9
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> range(1, 11)     # 从 1 开始到 10
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> range(0, 30, 5)  # 步长为 5
# [0, 5, 10, 15, 20, 25]
## as a result, when it comes to "2", range(2, 2) won't be evacuate.

# 5.____________________________________________________________
