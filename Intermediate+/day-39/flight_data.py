class FlightData:
    # This class is responsible for structuring the flight data.
    
    def __init__(self) -> None:
        self.departure_city = None
        self.arrival_city = None
        self.departure_date = None
        self.return_date = None
        self.lowest_price = 1000000.00     # at the first evaluation any flight will be cheaper than 1 million

    def find_cheapest_flight(self, flights_list):
        
        for flight in flights_list:
            if float(flight["price"]["grandTotal"]) < self.lowest_price:
                self.lowest_price = float(flight["price"]["grandTotal"])
                self.departure_city = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                self.arrival_city = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                self.departure_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                self.return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
