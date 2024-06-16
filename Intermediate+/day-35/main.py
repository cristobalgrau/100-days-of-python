import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables from .env file
load_dotenv()

MY_LAT = 29.424122
MY_LONG = -98.493629

api_key = os.environ.get('WEATHER_API_KEY')
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_phone = os.environ.get('TWILIO_PHONE_NUM')
receiver_phone = os.environ.get('RECEIVER_PHONE_NUM')

endpoint_url = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=endpoint_url, params=parameters)
response.raise_for_status()

forecast = response.json()["list"]

forecast_codes = [forecast[index]["weather"][0]["id"] for index in range(len(forecast))]

print(forecast_codes)

for code in forecast_codes:
    if code < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body="It's going to rain today. Remember to bring an Umbrella! ☂️",
                from_=twilio_phone,
                to=receiver_phone
            )
        print(message.status)
        break
