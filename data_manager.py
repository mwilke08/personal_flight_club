import requests
from pprint import pprint

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, url):
        self.airport_sheet = url

    def get_sheet(self):
        response = requests.get(url=self.airport_sheet)
        data = response.json()
        return data['prices']

    def set_iata_code(self, city, code):
        body = {
            "city": city,
            "iataCode": code,
        }
        response = requests.put(url=self.airport_sheet, json=body)
