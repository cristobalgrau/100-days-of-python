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
users_email = destinations.get_customer_emails()

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
    city = data["city"]
    iata_code = data["iataCode"]
    lowest_price = data["lowestPrice"]

    print(f"\nSearching for: {city}")
    available_flights = flight.get_flights(ORIGIN_CITY, iata_code, start_date, end_date)
    
    if available_flights:
        cheap_flight.find_cheapest_flight(available_flights)
        
        arrival_city = cheap_flight.arrival_city
        lowest_price_today = cheap_flight.lowest_price
        stops = cheap_flight.stops

        print(f"The lowest flight today to {arrival_city} is ${lowest_price_today} with "
              f"{stops} stop")
        
        if lowest_price_today < lowest_price:
            print(f"Found an offer to {arrival_city}. An email will be send it shortly.")
            subject = f"Found a flight offer to {arrival_city}"
            
            if stops == 0:
                message_body = (f"Low price Alert!. \n\n"
                                f"Found a Non-Stop Flight offer for only ${lowest_price_today} to fly "
                                f"from {cheap_flight.departure_city} to {arrival_city}, on "
                                f"{cheap_flight.departure_date} until {cheap_flight.return_date}.")
            else:
                message_body = (f"Low price Alert!\n\n"
                                f"Found a {stops}-stop Flight offer for only ${lowest_price_today} to fly "
                                f"from {cheap_flight.departure_city} to {arrival_city}, on {cheap_flight.departure_date} "
                                f"until {cheap_flight.return_date}.")
                
            notification.send_offers_email(users_email, subject, message_body)
        else:
            print("It is not the desired price!")
    else:
        print("No flights found!")

