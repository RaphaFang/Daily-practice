import pandas
str = "3_python_100daysChallenge/d26_list_comprehension/nato_phonetic_alphabet.csv"

data_nato = pandas.read_csv(str)
data = data_nato.to_dict()
nato_data_frame = pandas.DataFrame(data)

format_data = {row.letter:row.code for (index,row) in nato_data_frame.iterrows()}

name = list(input("What's your name?").upper())
# name_dict = {key:value for (key,value) in format_data.items() if name == format_data.items().key()}
output_list = [format_data[n] for n in name]
print(output_list)