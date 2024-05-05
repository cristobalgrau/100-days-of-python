# Day 17 - The Quiz Project & The Benefits of OOP

## Project: The Quiz Game

"The Quiz Game" is a command-line quiz application designed to test users' general knowledge with True or False questions. 
The project consists of four main files, each serving a specific purpose:

- `main.py`: This file serves as the entry point for the program. It contains the main program logic responsible for interacting with the user, managing the quiz flow, and keeping track of the user's score. It utilizes objects and functions defined in other files to achieve its functionality.
- `data.py`: The data.py file holds the question data used in the quiz. It contains a list of dictionaries, with each dictionary representing a question. Each question dictionary contains the text of the question and its corresponding answer (True or False).
- `question_model.py`: In this file, the Question class is defined. This class models each individual question in the quiz. It stores the text of the question and its answer as attributes. The Question class provides a structured way to represent question data within the program.
- `quiz_brain.py`: The quiz_brain.py file contains the QuizBrain class, which manages the quiz logic. This class is responsible for tracking question numbers, presenting questions to the user, checking user answers, and updating the user's score. It interacts with question data provided by the data.py file to conduct the quiz.

Object-oriented programming (OOP) principles are applied throughout the project, with classes such as Question and QuizBrain encapsulating related functionality. The modularization is achieved by splitting the program into multiple files, each handling a specific aspect of the application (data management, quiz logic, user interaction).
