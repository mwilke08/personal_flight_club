import requests
from pprint import pprint

FLIGHT_URL = "https://api.sheety.co/3871b3bd1969f6ec4c9cd8a5b99e7397/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destinations = {}

    def get_sheet(self):
        response = requests.get(url=FLIGHT_URL)
        data = response.json()
        self.destinations = data['prices']

        return self.destinations

    def set_code(self):
        for city in self.destinations:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{FLIGHT_URL}/{city['id']}", json=new_data)
            print("Success")
