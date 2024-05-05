# Day 11 - The Blackjack Capstone Project

## Project: Blackjack Game

This dynamic program simulates the popular casino game, allowing players to compete against the computer dealer in a battle of skill and luck.

### Gameplay Mechanics

The project adheres to classic Blackjack house rules, offering an authentic gaming experience. 

Key rules include:

- The deck is unlimited in size, with no jokers.
- Face cards (Jack, Queen, King) have a value of 10.
- Aces can count as either 11 or 1, depending on the player's choice.
- Players aim to achieve a hand value as close to 21 as possible without exceeding it (busting).
- The computer acts as the dealer, following a predefined set of rules for drawing cards.

### Core Functions

The project is structured around essential functions that handle core gameplay mechanics:

- `deal_card()`: Simulates dealing a card from the deck, selecting a random card value from a predefined list.
- `calculate_score()`: Computes the total score of a player's hand based on the sum of card values.
- `compare()`: Compares the final scores of the player and the computer to determine the winner.

### User Interaction

Players interact with the game through a command-line interface, which prompts them to make strategic decisions at various 
stages of the game. They can choose to draw additional cards (hit) or pass (stand), aiming to outscore the dealer without exceeding 21.
