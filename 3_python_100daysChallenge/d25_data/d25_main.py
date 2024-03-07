str = "3_python_100daysChallenge/d25_data/d25_weather_data.csv"
import csv

# with open(str) as file:
#     csv_list = file.readlines()
#     print(csv_list)
#     ## by using readlines(), it take the data into a list

# with open(str) as file:
#     csv_list = file.read()
#     print(csv_list)
    ## by using read(), it take the data into the order it used to be

# with open(str) as data_file:
#     data = csv.reader(data_file)
#     temperatures = []  ## it should outside the for loop
#     for n in data:
#         if n[1] != "temp":
#             temperatures.append(int(n[1]))
#     print(temperatures)


import pandas
data = pandas.read_csv(str)
# print(data["temp"])

data_dict = data.to_dict()
temp_list = data["temp"].to_list()

print(temp_list)


## Average
average = sum(temp_list)/len(temp_list)
print(average)
print(data["temp"].mean())

## the highest temp
print(data["temp"].max())

## get data in colums
print(data["condition"])
print(data.condition)

## get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

## get percisely the data of a row
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]

## create a different score from scratch
data_dict = {
    "student" : ["A", "B", "C"],
    "score" : [10, 20 ,30]
}
data_stu = pandas.DataFrame(data_dict)
data_stu.to_csv("new_data.csv")