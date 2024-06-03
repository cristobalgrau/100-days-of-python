import requests
from datetime import datetime
import time

MY_LAT = 29.760799      # Your latitude
MY_LONG = -95.369507    # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if -5 <= iss_latitude - MY_LAT <= 5 and -5 <= iss_longitude - MY_LONG <= 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour + 5      # Plus 5 because I am in Time Zone (GMT-5)
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)      # This will execute the loop every 60 seconds
    if is_iss_overhead() and is_night():
        # Should send email but for testing will only print
        print("Subject: Look Up\n\n The ISS is above you in the sky.")
