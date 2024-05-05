####### The Higher Lower Game but Instagram followers #######

import random
import art
from IPython.display import clear_output
from game_data import data

def random_option ():
    """ Generate a random personality from the date and return it as library"""
    return random.choice (data)

def artist_information (artist, option):
    """ Print on screen the option's information to choose"""
    print (f"Compare {option}: {artist['name']}, a {artist['description']}, from {artist['country']} ")

def compare_followers (user_option, second_option):
    """ Compare the followers and return TRUE if user wins"""
    if user_option > second_option:
        return True
    else:
        return False


print (art.logo)
option_a = random_option ()

game_over = False
score = 0
while not game_over:
    option_b = random_option ()
    # To be sure the random it does not give the same value
    while option_a == option_b:
        option_b = random_option ()
    
    artist_information (option_a, "A")
    print (art.vs)
    artist_information (option_b, "B")
    guess = input ("Who has more followers? Type 'A' or 'B': ").upper()

    if guess == "A":
        win = compare_followers (option_a['follower_count'], option_b['follower_count'])
        if win:
            score += 1
    elif guess == "B":
        win = compare_followers (option_b['follower_count'], option_a['follower_count'])
        if win:
            option_a = option_b
            score += 1
    else:
        win = False
        game_over = True
            
    clear_output ()
    print (art.logo)
    
    if win:
        print (f"You're right! Current score: {score}.")
    else:
        print (f"Sorry, that's wrong. Final score: {score}")
        game_over = True
