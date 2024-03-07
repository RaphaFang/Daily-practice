#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# with open("3_python_100daysChallenge/d24_hightScore_mailMerge/myfile.txt", mode='a') as file:
#     file.write('\nnew line')
# with open(str, mode='r') as file:
#         print(file.read())

with open("/Users/fangsiyu/Desktop/program/3_python_100daysChallenge/d24_hightScore_mailMerge/Mail Merge Project Start/Input/Names/invited_names.txt")as file:
      name_list = file.read().split()
    #   print(name_list)
      for name in name_list:
            with open("/Users/fangsiyu/Desktop/program/3_python_100daysChallenge/d24_hightScore_mailMerge/Mail Merge Project Start/Input/Letters/starting_letter.txt")as file:
                start_file = file.read()
                # print(type(start_file))
                start_file = start_file.replace("[name]", name)
                with open(f"{name}.txt", 'w')as file:
                    file.write(start_file)


# papapa = "I like bananas"
# x = papapa.replace("bananas", "apples")
# print(x)