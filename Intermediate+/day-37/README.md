# Day 37 - Habit Tracking Project: API Post Requests & Headers

## Project: Habit Tracker

The Habit Tracker project is designed to help users track their daily habits and visualize their progress using the Pixela API. Users can log, update, and delete their daily habit data, and view their habit tracking graph through a graphical user interface (GUI). The application leverages web requests to interact with the Pixela API and provides a simple and intuitive interface using Tkinter.


### Key Features:

- **User and Graph Creation**: Functions to create a Pixela user account and a habit-tracking graph.
- **Data Logging**: Capability to log daily habit data (e.g., minutes spent coding).
- **Data Management**: Functions to update and delete logged data.
- **Graph Visualization**: Open the Pixela habit tracking graph in a web browser.
- **GUI Integration**: A user-friendly interface for interacting with the habit tracker.


### Libraries Used:

- `requests`: For making HTTP requests to the Pixela API.
- `os`: For accessing environment variables.
- `dotenv`: For loading environment variables from a .env file.
- `datetime`: For handling date and time operations.
- `tkinter`: For creating the graphical user interface.
- `webbrowser`: For opening URLs in the web browser.


### Implementation:

**Environment Setup**

The application begins by loading environment variables from a `.env` file using load_dotenv. These variables include the Pixela API token, username, and graph ID, which are used to authenticate API requests.

**Pixela User and Graph Creation**

- Create Pixela User:
The `create_pixela_user` function sends a `POST` request to the Pixela API to create a new user with the specified token and username. The function includes the necessary parameters such as agreeing to the terms of service and confirming the user is not a minor.

- Create Pixela Graph:
The `create_pixela_graph` function creates a new graph for tracking habits. The graph configuration includes the graph ID, name, unit of measurement, type, and color. A `POST` request is sent to the Pixela API to create the graph.

**Pixel Management**

- Create Pixel:
The `create_pixel` function logs daily habit data by sending a `POST` request to the Pixela API. The function retrieves the date and quantity from the user inputs, converts the date to the required format, and sends the data to the API. If successful, a success message is displayed; otherwise, an error message is shown.

- Update Pixel:
The `update_pixel` function updates an existing habit data entry. It constructs the pixel update endpoint using the specified date and sends a `PUT` request with the updated quantity. The function handles the response to provide feedback to the user.

- Delete Pixel:
The `delete_pixel` function deletes a logged habit entry for a specified date by sending a `DELETE` request to the Pixela API. The function provides user feedback based on the success of the operation.


**GUI Integration**


 - The `Tkinter` library is used to create the graphical user interface. The main window is configured with padding and a title.
 - A canvas widget is used to display the application's logo.
 - Labels and entry widgets are provided for the user to input the date and quantity of the habit data.
 - Buttons are created to trigger the functions for creating, updating, and deleting pixels, as well as opening the Pixela habit tracking webpage.


### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/ebc73014-79f3-405b-b97b-c505c73a564d)

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/d0ef5550-4294-4463-b764-42bc0b98ad64)

