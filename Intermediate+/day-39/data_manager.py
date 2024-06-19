import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    endpoint = os.environ.get("SHEETY_ENDPOINT")
    token = os.environ.get("SHEETY_TOKEN")

    def __init__(self) -> None:
        self.headers = {"Authorization": "Bearer " + self.token}

    def get_cities(self):
        response = requests.get(url=self.endpoint, headers=self.headers)
        response.raise_for_status()

        return response.json()["prices"]

    def update_iata_code(self, sheety_id, code):
        put_endpoint = f"{self.endpoint}/{sheety_id}"

        data = {
            "price": {
                "iataCode": code,
            }
        }

        response = requests.put(url=put_endpoint, json=data, headers=self.headers)
        response.raise_for_status()
