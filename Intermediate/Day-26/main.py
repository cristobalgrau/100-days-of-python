# With the Nato Alphabet Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
# Ask to the user for a word and create a list with the corresponding nato phonetic alphabet with that word

import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {data.letter: data.code for (index, data) in nato.iterrows()}

word = input("Enter a word: ").upper()

#Create a list of the phonetic code words from a word that the user inputs.
phonetic_word = [nato_alphabet[letter] for letter in word]
print(f"Your phonetic letters are: {phonetic_word}")
