#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements
import data_manager
import flight_search

sheet = data_manager.DataManager()

sheet_data = sheet.get_sheet()

for data in sheet_data:
    if data['iataCode'] == '':
        new_code = flight_search.FlightSearch.search_code(city=data['city'])
        data_manager.DataManager.set_code(city=data['city'], code=new_code)

print(sheet_data)
