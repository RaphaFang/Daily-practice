# letter = "Rapha"
# letter_list = [n for n in letter]

# print(letter_list)

# double = range(1,5)
# double_list = [n*2 for n in double]
# print(double_list)


# name_list = []
# short_test = [name.upper() for name in name_list if len(name_list)>5]
# 1. __________________________________________________
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in  numbers]

print(squared_numbers)


# 2. __________________________________________________
list_of_strings = [9, 0, 32, 8, 2, 8, 64, 29, 42, 99]
result = [int(n) for n in list_of_strings if int(n)%2==0]

print(result)

# 3. __________________________________________________
with open("file1.txt") as file:
  list1 = file.readlines()
with open("file2.txt") as file:
  list2 = file.readlines()

result = [int(n) for n in list1 if n in list2]

print(result)

# 4. __________________________________________________
import random

names = ["aaa", 'bbb', 'ccc', 'ddd']
student_score = {student:random.randint(1,100) for student in names}
print(student_score)
passed_student = {student:score for (student, score) in student_score.items() if score>=60}
print(passed_student)

# 5. __________________________________________________
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}
print(result)

# 6. __________________________________________________
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {days:(f* 9/5) + 32 for (days, f) in weather_c.items()}

print(weather_f)

# 7. __________________________________________________
import pandas

student_dict = {"names":["aaa", "bbb", "ccc"],
                "scores":[10,20,30]}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
##  names  scores
# 0   aaa      10
# 1   bbb      20
# 2   ccc      30

for(index, row) in student_data_frame.iterrows():
    print(row)
        # names     aaa
        # scores     10
        # Name: 0, dtype: object
        # names     bbb
        # scores     20
        # Name: 1, dtype: object
        # names     ccc
        # scores     30
        # Name: 2, dtype: object
    print(row.names)
        # aaa
        # bbb
        # ccc