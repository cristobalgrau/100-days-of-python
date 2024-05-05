# Day 14 - Higher Lower Game Project

## Project: Higher Lower Game: Instagram Edition

In this captivating project, you'll put your knowledge of celebrity Instagram followers to the test as you compete to guess which 
personality boasts the highest follower count. 

### Gameplay Overview
The objective of the game is simple: compare the follower counts of two Instagram personalities and guess which one has the higher 
number of followers. 

Key features of the gameplay include:

- **Random Selection:**  Each round presents players with two randomly selected Instagram personalities, offering a diverse range of celebrities, influencers, and public figures to choose from.
- **Dynamic Interface:** A user-friendly interface guides players through each round, displaying essential information about each personality, including their name, description, and country of origin.
- **Interactive Guessing:** Players make their guess by selecting either option A or option B, indicating which personality they believe has the higher follower count. Correct guesses earn points and propel players to higher scores.

### Core Functions

The project is powered by essential functions that handle key game logic and user interaction:

- Random Option Selection: The `random_option()` function selects a random Instagram personality from the dataset, ensuring each round presents a unique set of options.
- Artist Information Display: The `artist_information()` function prints essential information about each Instagram personality, allowing players to make informed guesses based on their knowledge.
- Follower Count Comparison: The `compare_followers()` function compares the follower counts of two Instagram personalities and determines whether the player's guess is correct.

### Pseudocode generated to make the code

- Generate random choices for A and B and store them in variables
- Ask the user for the chosen option
- Compare if the user option is the highest
- If it's the highest, then store the user option as choice A. Increment counter of score
- Generate a new random choice B and ask the user to choose a new option
- If loose show the total score
