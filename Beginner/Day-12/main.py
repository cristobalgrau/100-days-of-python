###### Number Guessing Game #######

import random
from art import logo
from IPython.display import clear_output

def compare_numbers (number_guessed, number):
    """Compare the guessed number with the random number choosen"""
    if number_guessed == number:
        print (f"You got it!. The answer was {number}.")
        return True
    elif number_guessed > number:
        print ("Too high.")
    else:
        print ("Too low.")


def set_difficulty():
    """Determine the attempts according to the difficulty level chosen"""
    difficulty_levels = {"easy": 10, "hard": 5}
    difficulty = input ("Choose a difficulty, Type 'easy' or 'hard': ").lower()
    return difficulty_levels[difficulty]


def play_guessing_game():
    clear_output()
    print (logo)
    print ("Welcome to the Number Guessing Game!")
    print ("I'm thinking of a number between 1 and 100.")
    attempts = set_difficulty()
    
    number = random.randint(1, 100)

    win = False
    while attempts > 0 and not win:
        print (f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts -= 1
        win = compare_numbers (guess, number)
    
    if attempts == 0 and not win:
        print ("You've run out of guesses, you lose.")


repeat = True
while repeat:
    play_guessing_game()
    play_again = input("Do you want to play again?. Type 'y' or 'n': ").lower()
    if play_again == "n":
        repeat = False
