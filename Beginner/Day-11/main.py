############### Blackjack Project #####################

# Our Blackjack House Rules

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have an equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import art
from IPython.display import clear_output

def deal_card ():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice (cards)
    return random_card

def calculate_score (player_cards):
    score = 0
    for num in player_cards:
        score += num
    return score

def compare (user_points, computer_points):
    if user_points == computer_points:
        print ("draw")
    elif user_points > computer_points:
        print ("You win!")
    else:
        print ("You lose!")

def show_cards (user, user_score, computer, computer_score):
    print(f"\nYour cards: {user}, current score: {user_score}")
    if computer_score == 0:
        print(f"Computer's first card: {computer[0]}")
    else:
        print(f"Computer's final hand: {computer}, final score: {computer_score}")


new_game = True

while new_game:
    clear_output()
    print (art.logo)
    user_cards = []
    computer_cards = []
    
    for _ in range (0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    repeat_user = True
    game_over = False
    while repeat_user:
        user_score = calculate_score (user_cards)
        computer_score = calculate_score (computer_cards)
    
        show_cards(user_cards, user_score, computer_cards, 0)
        
        if computer_score == 21:
            show_cards(user_cards, user_score, computer_cards, computer_score)
            print ("You lose!, the opponent has Blackjack")
            game_over = True
            break
        elif user_score == 21:
            print ("You win!, you have Blackjack")
            game_over = True
            break
        elif user_score > 21:
            if 11 in user_cards:
                ace_index = user_cards.index(11)
                user_cards[ace_index] = 1
            else:
                print ("You went over. You lose!")
                game_over = True
                break
        else:
            repeat = input("Type 'y' to get another card, type 'n' to pass:  ").lower()
            if repeat == "n":
                repeat_user = False
            elif repeat == "y":
                user_cards.append(deal_card())
    
    while not game_over:
        if computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score (computer_cards)
        elif computer_score <= 21:
            show_cards(user_cards, user_score, computer_cards, computer_score)
            compare (user_score, computer_score)
            game_over = True
        elif computer_score > 21:
            show_cards(user_cards, user_score, computer_cards, computer_score)
            print("Opponent went over. You Win!")
            game_over = True

    repeat_game = input("\nDo you want to play another game of Blackjack? Type 'y' or 'n':  ").lower()
    if repeat_game == "n":
        new_game = False
