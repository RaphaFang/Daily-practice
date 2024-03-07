## 2023/12/26 
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

