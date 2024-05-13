# Day 26 - List Comprehension and the Nato Alphabet

## Project: NATO Alphabet

This is a Python application designed to convert user-inputted words into their corresponding NATO phonetic alphabet representation. 
The NATO phonetic alphabet, also known as the International Radiotelephony Spelling Alphabet, assigns a unique code word to each letter 
in the English alphabet to facilitate communication, especially in situations where clarity and precision are essential.

### Key Features:

- **Phonetic Translation:** Users can input any word, and the program will generate a list of corresponding NATO phonetic alphabet words for each letter in the word.
- **Data Handling:** The program utilizes the pandas library to read a CSV file containing the NATO phonetic alphabet data and creates a dictionary for efficient lookup.
- **Case Insensitivity:** The input word is converted to uppercase to ensure consistency and accuracy in the phonetic translation process.

### Libraries:

- `pandas`: Used for data manipulation, specifically for reading the NATO phonetic alphabet data from a CSV file.

### Implementation:

The application begins by prompting the user to enter a word. It then reads a CSV file containing the NATO phonetic alphabet data and creates a dictionary mapping 
each letter to its corresponding phonetic code, this is made using dictionary comprehension. After converting the user-inputted word to uppercase for consistency, 
the program generates a list of NATO phonetic alphabet words corresponding to each letter in the input word. Finally, the phonetic representation of the word is 
displayed to the user, providing a practical demonstration of the NATO Alphabet's utility in communication scenarios.

### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/e85bf9e9-44ff-409c-be88-c35351bd33f6)
