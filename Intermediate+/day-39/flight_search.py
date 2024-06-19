import requests
import os
from dotenv import load_dotenv

load_dotenv()


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    search_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    city_code_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

    def __init__(self) -> None:
        self.api_key = os.environ.get("AMADEUS_API_KEY")
        self.api_secret = os.environ.get("AMADEUS_API_SECRET")
        self.token = self.get_amadeus_token()
        self.headers = {"Authorization": "Bearer " + self.token}

    def get_amadeus_token(self):

        amadeus_header = {"content-type": "application/x-www-form-urlencoded"}
        amadeus_params = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        token_response = requests.post(url=self.token_url, headers=amadeus_header, data=amadeus_params)
        token_response.raise_for_status()

        if token_response.status_code == 200:
            return token_response.json()["access_token"]

    def get_iata_code(self, city, country):

        city_params = {
            "keyword": city,
            "countryCode": country,
            "max": 10,
            "include": "AIRPORTS"
        }

        city_response = requests.get(url=self.city_code_url, headers=self.headers, params=city_params)
        city_response.raise_for_status()

        # To manage no city IATA code found
        if city_response.json()["meta"]["count"] == 0:
            return False
        else:
            code = False
            for city_data in city_response.json()["data"]:
                try:
                    if city_data["name"] == city:
                        code = city_data["iataCode"]
                except:
                    continue
            return code

    def get_flights(self, origin_code, destination_code, departure_date, return_date):

        flight_params = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "USD",
            "max": 10
        }
         
        flights_response = requests.get(url=self.search_url, headers=self.headers, params=flight_params)
        flights_response.raise_for_status()

        # to manage no flights found
        if flights_response.json()["meta"]["count"] == 0:
            return False
        else:
            return flights_response.json()["data"]
