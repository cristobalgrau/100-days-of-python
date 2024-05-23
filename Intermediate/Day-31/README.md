# Day 31 - Flash Card App Capstone Project

## Project: Flash Card App

This project is a Flash Card App that helps users learn French vocabulary through interactive flashcards. 
The app displays a French word on the front side of the card and its English translation on the backside. 
Users can mark words they have learned, which will remove them from the learning list.

### Key Features

- **Interactive Flashcards:** Displays French words and their English translations on a timed flip mechanism.
- **Progress Tracking:** Allows users to remove words they have learned from the study set.
- **Data Persistence:** Saves the list of words to learn between sessions.

### Libraries

- `tkinter`: Used for creating the graphical user interface, including labels, buttons, and canvas elements.
- `pandas`: Handles the reading and writing of CSV files, which store the vocabulary words.
- `random`: Randomly selects flashcards from the list.

### Implementation

The Flash Card App is implemented using Python's tkinter library for the GUI and pandas for managing the vocabulary data.

The app attempts to load the `words_to_learn.csv` file. If it doesn't exist, the error is handled it with the `try` block and it falls back to loading `french_words.csv`. 
The data is then converted into a list of dictionaries of records. A function `random_flashcard` is defined to select a random word from the list of dictionaries, 
update the flashcard display, and set a timer to flip the card after 3 seconds, then the `flip_flashcard` function changes the flashcard to show the English translation.

The app has an interactive GUI where the user can select if the word is unknown, with the `X` button, or if the word is known by the user, by selecting the `✓` button. If the user selects the `X` button, 
the app calls again the `random_flashcard` function to show the next word. But, if the user selects the `✓` button then the word showed is removed from the list with the `remove_word` function and updates 
the available words into the CSV file `words_to_learn`, so the next time the user runs the App it will only show the unknown words, and after this update, the app will call again the next word with the 
`random_flashcard` function.

### Result

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/a6a0deda-f75c-499e-b123-0878821f6389)
