# Hangman Game Project

import random
import hangman_words
from hangman_art import logo, stages
from IPython.display import clear_output


chosen_word = random.choice (hangman_words.word_list)
word_length = len(chosen_word)
lives = 6

display = []
for _ in range (word_length):
    display.append ("_")

#print (hangman_art.logo) ----> This one is with import only not from xxx import
print (logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

while display.count("_") > 0 and lives > 0:
    guess = input("Guess a letter: ").lower()

    clear_output()

    if guess in display:
        print (f"You've already guessed {guess}!")

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess
    
    if guess not in chosen_word:
        lives -= 1
        print (f"You guessed {guess}, that's not in the word. You lose a life!.")
    
    #print (hangman_art.stages[lives]) ----> This one is with import only not from xxx import
    print (stages[lives])

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    
    if display.count("_") == 0:
        print ("You win!")
    elif lives == 0:
        print ("You lose!")
