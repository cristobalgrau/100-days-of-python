# Day 25 - Working with CSV Data and the Pandas Library

## Project: U.S. States Game

The US States Game is an interactive Python application that tests your knowledge of the United States' geography. 
It presents players with a blank map of the US states and prompts them to identify each state by typing its name. 
The game also offers a feature to save the list of missed states for further learning.

### Key Features:

- **Interactive Gameplay:** Players are presented with a blank map of the US states and are prompted to enter the name of each state they recognize.
- **State Identification:** The game accepts user input and checks if the entered state name is correct. If correct, the state name is displayed on the map.
- **Save Missed States:** Players have the option to save the list of states they missed for later learning, enhancing the educational value of the game.

### Libraries:

- `turtle`: Provides a graphics environment for creating interactive applications.
- `pandas`: Used for data manipulation, specifically for reading the list of US states from a CSV file.

### Implementation:

The game initializes with a blank map of the US states and prompts the player to enter the names of the states they recognize. 
The player's input is checked against a list of US states, and if correct, the state name is displayed on the map. The game continues 
until the player identifies all 50 states or chooses to exit. If the player exits, with the keyword `exit`, the list of missed states is saved to a CSV file 
named "states_to_learn.csv" for further study.

### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/0cc3a44d-c139-49cc-abf0-5a5b7a142aab)
