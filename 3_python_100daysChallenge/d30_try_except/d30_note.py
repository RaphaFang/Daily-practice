# FileNotFound

## try
try:
    file = open("3_python_100daysChallenge/d30/a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict)
    print(a_dict["aaa"])

except FileNotFoundError:
    file = open("b_file.txt", "w")
    file.write("sth")
    print("FileNotFoundError !!")

except KeyError as error_message:
    print(f"{error_message} doesn't exist")
    # this would output the actual error couzed the Keyerror
else: # this wold only be trigger, if the try statement work
    content = file.read()
    print(content)

finally:
    file.close()
    print("file closed")

    raise TypeError("the type error cuz by me")

## 272. __________________________________________________
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height shouldn't over 3ms")

bmi = weight / height**2
print(bmi)

## 273. quiz __________________________________________________
fruits = eval(input())

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
  try:
    fruit = fruits[index]
  except IndexError:
    print("Fruit pie")
  else:
    print(fruit + " pie")

make_pie(4) # Raises IndexError on list with less than 5 item


## 274. quiz __________________________________________________
facebook_posts = eval(input())

total_likes = 0
# TODO: Catch the KeyError exception
for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    pass


print(total_likes)