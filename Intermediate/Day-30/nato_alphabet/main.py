# With the Nato Alphabet Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
# Ask to the user for a word and create a list with the corresponding nato phonetic alphabet with that word

import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {data.letter: data.code for (index, data) in nato.iterrows()}

# ------- My approach to the solution for Error Handling ---------------
keep_trying = True
while keep_trying:
    word = input("Enter a word: ").upper()

    #Create a list of the phonetic code words from a word that the user inputs.
    try:
        phonetic_word = [nato_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(f"Your phonetic letters are: {phonetic_word}")
        keep_trying = False



# ------- The course Approach to the error handling------------------
# def generate_phonetic():
#     word = input("Enter a word: ").upper()
#
#     try:
#         phonetic_word = [nato_alphabet[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         generate_phonetic()
#     else:
#         print(f"Your phonetic letters are: {phonetic_word}")
# -------------------------------------------------------------------
