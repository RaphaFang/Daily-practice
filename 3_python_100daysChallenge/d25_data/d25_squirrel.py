import pandas
str = "3_python_100daysChallenge/d25_data/Squirrel.csv"
data = pandas.read_csv(str)

gray_s_num = len(data["Primary Fur Color"] == "Gray")
cinnamon_s_num = len(data["Primary Fur Color"] == "Cinnamon")
black_s_num = len(data["Primary Fur Color"] == "Black")

data_dict = {
    "Fur Color" : ["Gray","Cinnamon", "Black"],
    "Count" : [gray_s_num,cinnamon_s_num,black_s_num]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")