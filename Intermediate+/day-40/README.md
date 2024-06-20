# Day 40 - Capstone Part 2: Flight Club

## Project: The Flight Club

The Flight Club project is an update for the Day-39 project, where you create a spreadsheet with your user's information, like First Name, Last Name, and email, to create a diffusion list for the flight offers. 

The project aims to help users find the best flight deals and notify them via email when cheaper flights are available. It integrates with the Amadeus API to search for flights, the Sheety API to manage destination data, and the Gmail API to send notifications. The application retrieves flight information, compares prices, and notifies users when a good deal is found.

[Sheety API documentation](https://sheety.co/docs/requests)

[Amadeus API Documentation](https://developers.amadeus.com/self-service/apis-docs)

[Gmail API Python quickstart documentation](https://developers.google.com/gmail/api/quickstart/python?hl=en)


### Key Features:

- **Destination Data Retrieval**: Fetches destination data from a Google Sheet using the Sheety API.
- **IATA Code Update**: Updates destination data with IATA codes if missing.
- **Flight Search**: Searches for flights using the Amadeus API.
- **Cheapest Flight Detection**: Finds and records the cheapest available flight.
- **Notification**: Sends email notifications when a cheaper flight is found.


### Libraries:

- `requests`: For making HTTP requests to the Sheety and Amadeus APIs.
- `os`: For accessing environment variables.
- `dotenv`: For loading environment variables from a .env file.
- `datetime`: For handling date and time operations.
- `base64, email`: For handling email notifications.
- `google.auth, google_auth_oauthlib, googleapiclient`: For Gmail API integration.


### Implementation:

**Environment Setup**

The application begins by setting up the environment to manage sensitive information securely. This is achieved using the Python dotenv library, which loads environment variables from a `.env` file. The `.env` file contains critical information such as the Sheety API endpoints and token, Amadeus API credentials (API key and secret), and Twilio account SID, authentication token, phone numbers, and email details.

**Destination Data Management**

The first step in the application workflow is to retrieve and manage destination data. This is handled by the DataManager class, which interacts with a Google Sheet using the Sheety API. The following steps are performed:

1. **Retrieve Data**: The application fetches the list of destination cities and associated data from the Google Sheet.
2. **Update IATA Codes**: For cities that do not have an IATA code, the application uses the FlightSearch class to obtain the correct IATA code from the Amadeus API and updates the Google Sheet accordingly. This ensures that all destinations have the necessary data for flight searches.
3. **Retrieve Customer Emails**: The application also retrieves a list of customer emails from the Google Sheet to send notifications.

**Flight Data Retrieval**

The core functionality of the application is to search for flight deals. This is managed by the `FlightSearch` class, which communicates with the Amadeus API. The process involves:

1. **Obtain Access Token**: The application requests an access token from the Amadeus API using client credentials. This token is necessary for authenticating subsequent API requests.
2. **Search Flights**: For each destination, the application searches for flights using the origin city and the destination IATA code. The results are checked for any available flights.

**Cheapest Flight Analysis**

Once the flight data is retrieved, the application analyzes it to find the cheapest flight. This is performed by the `FlightData` class:

1. **Initialize Values**: Default values are set, including a high initial value of 1 million for the lowest price to ensure any valid flight will be considered cheaper.
2. **Find Cheapest Flight**: The application iterates through the list of available flights and updates the instance variables with details of the flight that has the lowest price.

**Notification Logic**

If a cheaper flight than the one recorded in the Google spreadsheet is found, the application sends an email and/or SMS notification to the user. This is managed by the NotificationManager class:

1. **Gmail API Integration**: The application uses the Gmail API to send email notifications. It authenticates using OAuth 2.0 and sends emails to the list of customer emails retrieved from the Google Sheet.
2. **Send Email**: An email message is created with the flight deal details and sent to each customer email using the Gmail API.


### Result:

**Spreadsheet data**

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/79940909-4f50-4bec-a948-58636f4e7ec2)

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/8af971d3-e9b5-4bcb-afb1-65fa97d1a840)


**Notifications**

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/e04b9bcc-a0a8-459c-9091-bac11da1cbe2)

**email bodies**

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/696dc783-a073-4498-ab32-a2b2a7b895ec)

