alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
input_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
input_text = input("Type your message:\n").lower()
input_shift = int(input("Type the shift number:\n"))

def caesar(direction, text, shift):
    if direction == "encode":
        new_position += shift
    else:
        new_position -= shift

def encrypt(text, shift):
    after_split_text = ""
    for x in text:
        position = alphabet.index(x)
        new_position = position + shift
        new_letter = alphabet[new_position]
        after_split_text += new_letter
    print(f"The encoded text is {after_split_text}")

def decrypt(text, shift):
    after_split_text = ""
    for x in text:
        position = alphabet.index(x)
        new_position = position - shift
        new_letter = alphabet[new_position]
        after_split_text += new_letter
    print(f"The encoded text is {after_split_text}")


    if input_direction == "encode":
        encrypt(text=input_text, shift=input_shift)
    else:
        decrypt(text=input_text, shift=input_shift)
