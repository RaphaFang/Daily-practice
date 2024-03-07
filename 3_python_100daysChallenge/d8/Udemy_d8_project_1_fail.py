alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
input_text = input("Type your message:\n").lower()
input_shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    after_split_item = []
    after_split_text = ""
    for n in range(0, len(text)):
        after_split_item += text[n]
        for x in range(0,len(after_split_item)):
            after_split_item[x] = alphabet[x+shift]
        after_split_text += after_split_item[x]
            

    print(f"The encoded text is {after_split_text}")
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

encrypt(text=input_text, shift=input_shift)


## fail
## this wont give the correct encrypt "ace" to "cef" 
## learn the "index" func.