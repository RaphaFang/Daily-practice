from art import logo
print(logo)

def caesar(direction, text, shift):
    after_split_text = ""
    for x in text:
        if x in alphabet:
            position = alphabet.index(x)
            if direction == "encode":
                position += shift
            else:
                position -= shift
            new_letter = alphabet[position]
            after_split_text += new_letter
        else:
            after_split_text += x
    print(f"The encoded text is {after_split_text}")

going = True
while  going == True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    input_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    input_text = input("Type your message:\n").lower()
    input_shift = int(input("Type the shift number:\n"))%26
    caesar(direction=input_direction, text=input_text, shift=input_shift)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if result == "no":
        going = False
        print("Goodbye.")
    
## last part, deal with 
## 1.logo 
## 2.the big number problem 
## 3.dont convert beside the alphabet
## keep running the program
