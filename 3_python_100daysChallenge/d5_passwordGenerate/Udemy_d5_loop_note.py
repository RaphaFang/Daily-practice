# 1.____________________________________________________________
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# x = 'runoob'
# >>> for i in range(len(x)) :
# ...     print(x[i])
# r
# u
# n
# o
# o
# b
    

# 2.____________________________________________________________
student_heights = input().split()
# print(student_heights) = ['151', '145', '179']
# print(len(student_heights)) = 3
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights) = [151, 145, 179]

total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")
## round(A/B), will output a num without dicimal points. "四捨五入" is runding in english.


# 3.____________________________________________________________
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# Write your code below this row 👇
highest_score =0
for score in student_scores:
  highest_score = score
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")


# 4.____________________________________________________________
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Your code below this row 👇
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score


# 5.____________________________________________________________
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️
# Write your code here 👇
total = 0
for num in range(2,target+1,2):
  total += num
print(total)


# 6.____________________________________________________________
for n in range(1, 101):
  if n%5==0 and n%3==0:
    print("FizzBuzz")
  elif int(n)%5 == 0:
    print("Buzz")
  elif int(n)%3 == 0:
    print("Fizz")
  else:
    print(n)

# 7.____________________________________________________________
