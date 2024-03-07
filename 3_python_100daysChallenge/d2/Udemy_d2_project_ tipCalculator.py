# What I learned?
# 1. the num you get from input function, is "str"
# 2. the way to int/float a "str" is to used in a prompt, 
# 2.1. not type in a new line like "int(tip_percentage)" directly
# 2.2. either using "type(tip_percentage)"
# 3.1 but "print()" & "name a variable" would help.
# 3.2 e.g. "year = int(input())"

# ____________________________________________________________
print("Welcome to the tip calculator.")
your_bill = input("What is your total bill?\n$")
number_of_people = input("How many people joined the meal?\n")
tip_percentage = input("What percentage tip would you like to offer? (e.g. 10% please type 10. )\n")


# type(int(tip_percentage))
# print(type(int(tip_percentage)))


actual_tip = (1 + int(tip_percentage)*0.01)
after_divide = round((float(your_bill)/int(number_of_people))*float(actual_tip), 2)
after_divide = "{:.2f}".format(after_divide)
print(f"After calculate, each person should pay: ${after_divide}")

# Require
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇