#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements
from data_manager import DataManager
from flight_search import FlightSearch

sheet = DataManager()
flight_search = FlightSearch()

sheet_data = sheet.get_sheet()

for city in sheet_data:
    city['iataCode'] = flight_search.search_code(city['city'])

    sheet.destinations = sheet_data
    sheet.set_code()

print("All updated!")
