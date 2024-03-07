## what have I learned?
## function "type", it could check the type of data it is
## function "str", 

# 1.____________________________________________________________
two_digit_number = input()
print(type(two_digit_number))
str(two_digit_number)
print(two_digit_number[0] + two_digit_number[1])

## the output will be "1st_num_2nd_num"

# 2.____________________________________________________________
two_digit_number = input()
print(type(two_digit_number))
str(two_digit_number)
print(int(two_digit_number[0]) + int(two_digit_number[1]))

## the output will be "1st_num + 2nd_num"(it work finally...)

# 3.____________________________________________________________
height = input()
weight = input()
BMI = int(weight)/(float(height)**2)
print(int(BMI))

##if I don't put a "int" infront of the BMI, the defult output will be a float.


# 4.____________________________________________________________
age = input()
week_left = 4680-(int(age)*52)
print(f"You have {week_left} weeks left.")

## divide, always turn the num into "float"
## the "//" & "round function", have the same function, turn the num into "int", delete the decimal point.
    ## put a print(round(8/3, "2")) will limit the decimal point to 2nd.
    ## and this example, the function round chang the second decimal point, into 7.
## f-print, a easy way to print a string with var inside.


# 5.____________________________________________________________
## mistake I made 
age = 12
print("A" + age + "B")
## Age is an integer. You are trying to concatenate a String to an Integer.
## print function could only work on "string"
# instead, use "printf"
age = 12
print(f"A" + {age} + "B")
# uncorrect way to use printf
age = 12
print(f"A +{age}+ B")
# the printf function will keep the blank inside the the ().