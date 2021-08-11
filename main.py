#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements
import data_manager
import flight_search

sheet = data_manager.DataManager(url="https://api.sheety.co/3871b3bd1969f6ec4c9cd8a5b99e7397/flightDeals/prices")

sheet_data = sheet.get_sheet()


for data in sheet_data:
    if data['iataCode'] == '':
        iataCode = flight_search.FlightSearch.search_code(city=data['city'])
        data_manager.DataManager.set_iata_code(self=data, city=data['city'], code=iataCode)

print(sheet_data)