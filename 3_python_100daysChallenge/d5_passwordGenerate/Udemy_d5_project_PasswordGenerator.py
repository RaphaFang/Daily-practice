print("Welcome to the PyPassword Generator!")
num_of_l = int(input("How many letters would you like in your password?\n"))
num_of_s = int(input("How many symbols would you like?\n"))
num_of_n = int(input("How many numbers would you like?\n"))

# letter_string = input().split()
# print(letter_string)
all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
all_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
all_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
import random

password = ""
c_password = ""

for n in range(1, num_of_l+1):  
    # random_letter = all_letters[random.randint(0, 51)]     (also work...)
    password = random.choice(all_letters)
    c_password += password + " "

for n in range(1, num_of_s+1):  
    password = random.choice(all_numbers)
    c_password += password + " "

for n in range(1, num_of_n+1):  
    password = random.choice(all_symbols)
    c_password += password + " "
print(c_password)
hardpassword = ""
c_password = c_password.split()
print(c_password)


for n in range(1, len(c_password)+1):
    hardpassword += random.choice(c_password)
print(f"Your password is :\n {hardpassword}")


## "for n in range(1, num_of_n+1):  "
##      password += random.choice(all_symbols)
## you could take "range" as the amount of the "n"
## "n" manage the exacuat times of the string after the "tab" of the for str, 