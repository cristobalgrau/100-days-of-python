# Day 39 - Capstone Part 1: Flight Deal Finder

## Project: Flight Deal Finder - Part 1

The Flight Deal Finder project is designed to help users find the best flight deals and send notifications when cheaper flights are available. It integrates with the Amadeus API to search for flights and the Twilio API to send notifications via SMS. The application retrieves flight information, compares prices, and notifies users when a good deal is found.

[Sheety API documentation](https://sheety.co/docs/requests)

[Amadeus API Documentation](https://developers.amadeus.com/self-service/apis-docs)

### Key Features:

- **Destination Data Retrieval**: Fetches destination data from a Google Sheet using the Sheety API.
- **IATA Code Update**: Updates destination data with IATA codes if missing.
- **Flight Search**: Searches for flights using the Amadeus API.
- **Cheapest Flight Detection**: Finds and records the cheapest available flight.
- **Notification**: Sends SMS notifications when a cheaper flight is found.


### Libraries:

- `requests`: For making HTTP requests to the Sheety and Amadeus APIs.
- `os`: For accessing environment variables.
- `dotenv`: For loading environment variables from a `.env` file.
- `twilio`: For sending SMS notifications.
- `datetime`: For handling date and time operations.


### Implementation:

**Environment Setup**

The application begins by setting up the environment to manage sensitive information securely. This is achieved using the python `dotenv` library, which loads environment variables from a `.env` file. The `.env` file contains critical information such as the Sheety API endpoint and token, Amadeus API credentials (API key and secret), and Twilio account SID, authentication token, and phone numbers. 

**Destination Data Management**

The first step in the application workflow is to retrieve and manage destination data. This is handled by the `DataManager` class, which interacts with a Google Sheet using the Sheety API. The following steps are performed:

1. **Retrieve Data**: The application fetches the list of destination cities and associated data from the Google Sheet.
2. **Update IATA Codes**: For cities that do not have an IATA code, the application uses the FlightSearch class to obtain the correct IATA code from the Amadeus API and updates the Google Sheet accordingly. This ensures that all destinations have the necessary data for flight searches.

**Flight Data Retrieval**

The core functionality of the application is to search for flight deals. This is managed by the `FlightSearch` class, which communicates with the Amadeus API. The process involves:

1. **Obtain Access Token**: The application requests an access token from the Amadeus API using client credentials. This token is necessary for authenticating subsequent API requests.
2. **Search Flights**: For each destination, the application searches for flights using the origin city and the destination IATA code. The results are checked for any available flights.

**Cheapest Flight Analysis**

Once the flight data is retrieved, the application analyzes it to find the cheapest flight. This is performed by the `FlightData` class:

1. **Initialize Values**: Default values are set, including a high initial value of 1 million for the lowest price to ensure any valid flight will be considered cheaper.
2. **Find Cheapest Flight**: The application iterates through the list of available flights and updates the instance variables with details of the flight that has the lowest price.

**Notification Logic**

If a cheaper flight than the one recorded in the Google spreadsheet is found, the application sends an SMS notification to the user. This is managed by the `NotificationManager` class:

1. **Initialize Twilio Client**: The application sets up a Twilio client using the account SID and authentication token from environment variables.
2. **Send SMS**: An SMS message is created with the flight deal details and sent using the Twilio API. The message includes information about the departure city, arrival city, departure date, return date, and flight price.

### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/5c3931f9-2d72-4bb8-b1bc-d3fa4d1c0f05)

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/6a942b50-e244-48dd-951a-5206be6c7bed)


