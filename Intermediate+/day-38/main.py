import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Nutritionix API guide: https://docx.syndigo.com/developers/docs/nutritionix-api-guide
# Sheety documentation: https://sheety.co/docs/requests

load_dotenv()

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
sheety_url = os.environ.get("SHEETY_ENDPOINT")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

params = {
    "query": input("Tell me which exercises you did: ")
}

response = requests.post(url=nutritionix_endpoint, headers=nutritionix_headers, json=params)
response.raise_for_status()

workout_list = response.json()["exercises"]

sheety_headers = {"Authorization": "Bearer " + SHEETY_TOKEN}

for index in range(len(workout_list)):
    data = {
        "workout": {
            "date": datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": workout_list[index]["name"],
            "duration": workout_list[index]["duration_min"],
            "calories": workout_list[index]["nf_calories"]
        }
    }

    sheety_response = requests.post(sheety_url, json=data, headers=sheety_headers)
    sheety_response.raise_for_status()

    print(sheety_response.text)
