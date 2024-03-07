str = "/Users/fangsiyu/Desktop/program/3_python_100daysChallenge/d24_hightScore_mailMerge/myfile.txt"
# file = open (str)
# content = file.read()
# print(content)


## a stands for 'append'
## w stand to wrip all the content amd write
with open(str, mode='a') as file:
    file.write('\nnew line')
    with open(str, mode='r') as file:
        print(file.read())



with open("new_file.txt", mode='a') as file:
    file.write('\nwhere\'s it??')
# ## 他會直接將檔案創建在整體的最前方資料夾？？？
#     ##不懂這邏輯


with open("3_python_100daysChallenge/d24_hightScore_mailMerge/myfile.txt", mode='a') as file:
    file.write('\nnew line')
with open(str, mode='r') as file:
        print(file.read())

