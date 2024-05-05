import art
from IPython.display import clear_output

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar (plain_text, shift_amount, direction_value):
    
    # Creation of a new list with letters shifted
    shifted_alphabet = []
    for index in range (shift_amount, len(alphabet)):
        shifted_alphabet += alphabet [index]
    for index in range (shift_amount):
        shifted_alphabet += alphabet [index]

    new_text = ""
    if direction_value == "encode":
        for letter in plain_text:
            if letter in alphabet:
                new_text += shifted_alphabet[alphabet.index(letter)]
            else:
                new_text += letter                
        
    elif direction_value == "decode":
        for letter in plain_text:
            if letter in shifted_alphabet:
                new_text += alphabet[shifted_alphabet.index(letter)]                
            else:
                new_text += letter

    print (f"The {direction_value}d text is {new_text}")


repeat = "yes"

while repeat == "yes":
    clear_output()
    print (art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % (len(alphabet))
    caesar (text, shift, direction)
    repeat = input ("\nType 'yes' if you want to go again. Otherwise type 'no'.").lower()
