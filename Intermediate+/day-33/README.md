# Day 33 - API Endpoints & API Parameters - ISS Overhead Notifier

This day we made 2 projects. Project #1: Kanye Quotes App and Project #2: ISS Overhead Notifier. On these project we made use of API call to obtain data and managed it inside our projects.

## Project #1: Kanye Quotes App

The Kanye Quote App fetches quotes from the Kanye Rest API and displays them in a user-friendly graphical interface created using the Tkinter library.

### Key Features:

- **Fetch Quotes**: Retrieves random Kanye West quotes from an external API.
- **Display Quotes**: Shows the fetched quote on a graphical canvas.
- **User Interaction**: Allows users to fetch a new quote by clicking a button.

### Libraries:

- `Tkinter`: Used to create the graphical user interface (GUI).
- `requests`: Utilized for making HTTP requests to the Kanye Rest API.

### Implementation:

The Kanye Quote App is implemented using the following structure and functions:

**Fetching Quotes**:

The `get_quote` function makes a `GET` request to the Kanye Rest API, retrieves a random quote in json format, and updates the canvas to display the quote. It handles any HTTP errors that might occur during the request with the method `response.raise_for_status()`.

**Setting Up the User Interface**:
The UI is created using Tkinter. The main window is configured with padding for better aesthetics. A canvas widget is used to display the background image and the quote text. A button with an image of Kanye West is added to allow users to fetch a new quote when clicked.

### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/60bb694c-4355-4329-9f8d-c90ce7648155)


## Project #2: ISS Overhead Notifier

The ISS Overhead Notifier is a Python script designed to notify users when the International Space Station (ISS) is passing overhead during the night. The script continuously checks the ISS's position and the local time to determine if it is night and if the ISS is visible from the user's location.

### Key Features:

- **ISS Position Check**: Uses the Open Notify API to get the current position of the ISS.
- **Night Time Check**: Uses the Sunrise-Sunset API to determine if it is currently night at the user's location.
- **Continuous Monitoring**: The script runs in a loop, checking the conditions every 60 seconds.
- **Notification**: Prints a notification message when the ISS is overhead during the night. It could send an email using the previous script from `day-32` and host the script in the cloud to keep running the whole day.

### Libraries and Functions:
- `requests`: Utilized for making HTTP requests to the APIs.
- `datetime`: Used to handle date and time operations.
- `time`: Used to add delay in the continuous loop.

### Implementation:

**Checking ISS Position**:

The `is_iss_overhead` function makes a `GET` request to the Open Notify API to get the current latitude and longitude of the ISS. It then checks if the ISS is within a certain range (±5 degrees) of the user's location.

**Checking if it's Night**:

The `is_night` function makes a `GET` request to the Sunrise-Sunset API to get the times for sunrise and sunset at the user's location. It then checks if the current time is after sunset or before sunrise.

**Main Loop**:

The script runs in an infinite loop, checking the conditions every 60 seconds. If both conditions, ISS overhead and nighttime, are met, it prints/sends a notification message.

### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/cf824b58-ed49-4b53-adfc-f84a1e54af83)

