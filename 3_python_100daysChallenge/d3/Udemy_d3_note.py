# height > 180, means height should more than 180, only 181 and above would pass
# percisely X, you should type "==", "!=" not equals to.

# 1.____________________________________________________________

number = int(input())
if number%2 >= 1:
  print("This is an odd number.")
else:
  print("This is an even number.")

# 2.____________________________________________________________
height = float(input())
weight = int(input())

BMI = weight/height**2
actual_BMI = BMI

if float(BMI) < 18.5:
  BMI = str("are underweight")
elif float(BMI) < 25:
  BMI = str("have a normal weight")
elif float(BMI) < 30:
  BMI = str("are slightly overweight")
elif float(BMI) < 35:
  BMI = str("are obese")
else:
  BMI = str("are clinically obese")

print(f"Your BMI is {actual_BMI}, you {BMI}.")
## be careful that the ":" should add after the "if" & "elif" prompt.
## "else" should not add any promt after it, just":".

# 3.____________________________________________________________
year = int(input())
if year%4 == 0:
  if year%100 == 0:
    if year%400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
## A equal to B, you have to use "==" to express
  
# 4.____________________________________________________________
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

bill = 0

if size =="S":
  bill += 15
  if add_pepperoni =="Y":
    bill += 2
  if extra_cheese =="Y":
    bill +=1
elif size =="M":
  bill += 20
  if add_pepperoni =="Y":
    bill += 3
  if extra_cheese =="Y":
    bill +=1
else:
  size=="L"
  bill += 25
  if add_pepperoni =="Y":
    bill += 3
  if extra_cheese =="Y":
    bill +=1

print(f"Your final bill is: ${bill}.")

## if you want to detect a "str" from input for futher if/else function, 
## you have to  use "name == "A" "

# 5.____________________________________________________________
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

combin = (str(name1 + name2)).lower()
t_num = combin.count("t")
r_num = combin.count("r")
u_num = combin.count("u")
e_num = combin.count("e")
Total_T = t_num+r_num+u_num+e_num
l_num = combin.count("l")
o_num = combin.count("o")
v_num = combin.count("v")
e_num = combin.count("e")
Total_L = l_num+o_num+v_num+e_num

lovescore = str(Total_T)+str(Total_L)
          
if int(lovescore) < 10 or int(lovescore) > 90:
  print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif int(lovescore) > 40 and int(lovescore) <50:
  print(f"Your score is {lovescore}, you are alright together.")
else:
  print(f"Your score is {lovescore}.")

## function ".lower()" & ".count("t")"
## https://www.w3schools.com/python/ref_string_lower.asp
## https://www.w3schools.com/python/ref_list_count.asp
  