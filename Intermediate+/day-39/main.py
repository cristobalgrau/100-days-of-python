import datetime as dt

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

ORIGIN_CITY = "IAH"     # Houston's IATA Code


destinations = DataManager()
flight = FlightSearch()
cheap_flight = FlightData()
notification = NotificationManager()

# ----- Get destinations data from Spreadsheet -----

sheet_data = destinations.get_cities()

for data in sheet_data:
    if data["iataCode"] == "":
        city_name = data["city"]
        country = data["country"]
        city_id = data["id"]
        iata_code = flight.get_iata_code(city_name, country)
        if iata_code:
            destinations.update_iata_code(city_id, iata_code)
            data["iataCode"] = iata_code            # to save another request
        else:
            print(f"No Airport code found for {city_name}.")
            sheet_data.remove(data)

# ----- Get Flight offers -----

start_date = str(dt.date.today() + dt.timedelta(days=1))
end_date = str(dt.date.today() + dt.timedelta(days=180))

for data in sheet_data:
    print(f"\nSearching for: {data["city"]}")
    available_flights = flight.get_flights(ORIGIN_CITY, data["iataCode"], start_date, end_date)
    if available_flights:
        # cheap_flight = FlightData()
        cheap_flight.find_cheapest_flight(available_flights)
        print(f"The lowest flight today to {cheap_flight.arrival_city} is ${cheap_flight.lowest_price}")
        if cheap_flight.lowest_price < data["lowestPrice"]:
            print(f"Found an offer to {cheap_flight.arrival_city}. A SMS will be send it shortly.")
            message_body = (f"Low price Alert!. Only ${cheap_flight.lowest_price} to fly from "
                            f"{cheap_flight.departure_city} to {cheap_flight.arrival_city}, on "
                            f"{cheap_flight.departure_date} until {cheap_flight.return_date}.")
            notification.send_sms(message_body)
        else:
            print("It is not the desired price!")
    else:
        print("No flights found!")
