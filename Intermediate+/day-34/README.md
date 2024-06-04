# Day 34 - API Practice - Creating a GUI Quiz App

## Project: Trivia Question GUI using APIs

The Trivia Question project is an application designed to fetch and display trivia questions using a graphical user interface (GUI). The application fetches trivia questions from [Open Trivia Database API](https://opentdb.com/api_config.php), presents them to the user, and keeps track of the user's score based on their answers. The project is divided into five files, each responsible for different aspects of the application's functionality.

### Key Features:

- **Data Fetching**: Retrieves trivia questions from the Open Trivia Database API.
- **Question Processing**: Parses and stores questions in a usable format.
- **User Interface**: Provides an interface for users to answer trivia questions.
- **Score Tracking**: Tracks the user's score based on their answers.
- **User Feedback**: Provides visual feedback based on the user's answers.

### Libraries:
- `requests`: Used to make HTTP requests to the trivia API.
- `tkinter`: Used to create the graphical user interface.
- `html`: Used to unescape HTML entities in the questions. It helps to replace the reserved HTML characters with its original character representation.
- `csv`: Used for reading and writing CSV files.
- `random`: Used for random selection in some cases.

### Implementation:

The project consists of five key files:

- data.py
- question_model.py
- quiz_brain.py
- ui.py
- main.py

Each file has a distinct role in the overall functionality of the application, ensuring modularity and ease of maintenance.

**Data Retrieval (`data.py`)**

The `data.py` file is responsible for fetching trivia questions from an external API. The requests library is used to make an HTTP GET request to the Open Trivia Database API. The query parameters specify that ten questions of the boolean type are to be retrieved. After making the `GET` request, the `JSON` response is parsed to extract the list of questions, which is then stored in the question_data variable.

**Question Model (`question_model.py`)**

The `Question class` defined in `question_model.py` is a simple data structure that holds the question text and the correct answer. This encapsulation makes it easy to manage and pass around question data within the application.

**Quiz Logic (`quiz_brain.py`)**

The QuizBrain class in `quiz_brain.py` manages the flow of the quiz. It maintains the list of questions, tracks the current question number, and keeps the user's score. 

**User Interface (`ui.py`)**

The `QuizInterface` class in `ui.py` creates and manages the GUI using the tkinter library. The main window is configured with a title, background color, and padding. The interface includes a label to display the user's score, a canvas to display the current question, and buttons for the user to submit their answers. 

**Main Application (`main.py`)**

The `main.py` file serves as the entry point for the application. It imports the necessary modules and initializes the core components. It starts by creating a list of Question objects from the question_data. Each Question object is instantiated with a question text and the correct answer. This list, `question_bank`, is then passed to the `QuizBrain` class, which handles the quiz logic. Additionally, an instance of `QuizInterface` is created to manage the GUI.

### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/9a7a18be-d2f6-435f-9ded-36074f1c1864)

