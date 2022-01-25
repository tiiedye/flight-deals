from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()

for data in sheet_data:
    if data["iataCode"] == "":
        data["iataCode"] = flight_search.get_destination_code(data['city'])
        response = data_manager.update_destination_code(id=data["id"], iata=data["iataCode"])
