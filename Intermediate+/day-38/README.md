# Day 38 - Workout Tracking Using Google Sheets

## Project: Workout Tracking

The Workout Tracking project is designed to help users log their workout activities and track their fitness progress. It uses the Nutritionix API to analyze exercise data in a Natural Language prompt and the Sheety API to store the workout information in a Google Sheet. The application takes user input for the exercises performed, retrieves detailed exercise data, and logs this data into a spreadsheet for easy tracking and analysis.

[Nutritionix API guide](https://docx.syndigo.com/developers/docs/nutritionix-api-guide)

[Sheety documentation](https://sheety.co/docs/requests)

### Key Features

- **User Input for Exercises**: Prompts the user to enter the exercises they performed.
- **Exercise Data Retrieval**: Uses the Nutritionix API to get detailed information about the exercises.
- **Data Logging**: Logs the exercise data into a Google Sheet using the Sheety API.
- **Timestamped Entries**: Records the date and time of each exercise entry.


### Libraries:

- `requests`: For making HTTP requests to the Nutritionix and Sheety APIs.
- `os`: For accessing environment variables.
- `dotenv`: For loading environment variables from a `.env` file.
- `datetime`: For handling date and time operations.


### Implementation

**Environment Setup**

The load_dotenv function from the dotenv library is used to load environment variables from a .env file. This includes sensitive information such as the Nutritionix API App ID (APP_ID), API key (API_KEY), Sheety API token (SHEETY_TOKEN), and Sheety endpoint URL (SHEETY_ENDPOINT).

**Retrieve data**

The application first prompts the user to enter the exercises they performed in a Natural Language manner using the input function, later the Nutritionix API endpoint will process the input and extract the exercises performed by the user through a `POST` request. The API response is checked for errors using `response.raise_for_status()`, and if successful, the exercise data is extracted from the response JSON and stored in a variable.

**Logging data**

The application iterates over each exercise in the list and processes the data to format them to be ready to store them. For each exercise, a POST request is made to the Sheety API with the exercise data.

The API response is checked for errors using `sheety_response.raise_for_status()`, and if successful, the response text is printed to the console to provide feedback to the user. This feedback confirms whether the data was successfully logged, ensuring the user is informed of the application's status.


### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/e913da57-2c8d-4233-a6b6-66172c7e4b3c)

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/dc94c747-9fab-4d79-a79c-373e2581b4ec)

