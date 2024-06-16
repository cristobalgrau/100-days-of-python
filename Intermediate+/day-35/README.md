# Day 35 - Keys, Authentication & Environment Variables: Send SMS

## Project: Weather Notification

The Weather Notification project is a Python application designed to send weather alerts via SMS. It uses the OpenWeatherMap API to fetch weather data and Twilio's messaging service to send notifications if rain is expected. This project demonstrates how to integrate external APIs to create a functional application.

### Key Features:

- **Weather Forecast Retrieval**: Fetches weather data for a specified location.
- **Rain Detection**: Analyzes forecast data to detect rain.
- **SMS Notifications**: Sends an SMS alert if rain is predicted.
- **Environment Variable Management**: Securely handles sensitive information like API keys and authentication tokens.

### Libraries:

- `requests`: To make HTTP requests to the OpenWeatherMap API.
- `os`: For accessing environment variables.
- `dotenv`: To load environment variables from a `.env` file.
- `twilio`: To send SMS notifications.

### Implementation:

**Environment Setup**

The application starts by setting up the environment to securely manage sensitive information. This is achieved using the `python-dotenv` library, which loads environment variables from a .env file. This file contains the API key for OpenWeatherMap, Twilio account SID, authentication token, and phone numbers. By loading these values into the environment, the application ensures that sensitive information is not hard-coded in the source code.

**Weather Data Retrieval**

Next, the application retrieves weather data for a specified location using the OpenWeatherMap API. It constructs a request with specific parameters, including the latitude and longitude of the location and the number of forecast intervals to retrieve. The requests library is used to send this HTTP GET request to the API endpoint. Upon receiving the response, the application checks for any HTTP errors to ensure that the request was successful. The weather data, particularly the forecast for the next few hours, is then extracted from the response JSON.

**Forecast Analysis**

With the forecast data in hand, the application analyzes the weather conditions to detect the possibility of rain. It iterates through the list of weather forecasts, extracting weather condition codes for each time interval. These codes are numerical indicators provided by the OpenWeatherMap API that describe various weather conditions, as follows:

    - ID Group 2XX: Thunderstorm
    - ID Group 3XX: Drizzle
    - ID Group 5XX: Rain
    - ID Group 6XX: Snow
    - ID Group 7XX: Atmosphere (Mist, Haze, Dust, Fog, etc)
    - ID Group 800: Clear
    - ID Group 80X: Clouds

  [OpenWeatherMap Weather condition codes](https://openweathermap.org/weather-conditions)

By comparing these codes against a threshold (codes less than 700 typically indicate precipitation), the application determines if rain is expected in the forecast period.

**Notification Logic**

If the analysis detects rain, the application proceeds to send an SMS notification to the user. This is done using the Twilio API. The application initializes a Twilio client with the account SID and authentication token obtained from the environment variables. It then creates and sends an SMS message, using the pre-configured Twilio phone number to send the alert to the recipient's phone number.
  
### Issues found:

During the Twilio creation account, you will find that Twilio now requests that you have to make a "Toll-free verification", this is required for US messaging, according to their [new restriction](https://help.twilio.com/articles/20212966914075-Toll-Free-Verification-and-Developers-Navigating-the-New-Restrictions)

In my case, the Toll-Free verification was rejected on the first try because they were requesting company information to do the approval. I resubmitted the request but pointed out in the reason's description of the form that this is intended to send notifications to myself, and luckily it was approved the next day. I can't say this is the real solution or if was by luck

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/44becc88-e64d-402d-94b2-4c55428e119f)

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/7a24f3a9-46bd-4041-85eb-c2837e760e43)


### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/b94262e8-91b8-44f7-8ed0-43e6c497831f)







