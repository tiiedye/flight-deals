from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

for data in sheet_data:
    if data["iataCode"] == "":
        data["iataCode"] = flight_search.get_destination_code(data['city'])
        response = data_manager.update_destination_code(id=data["id"], iata=data["iataCode"])

tomorrow = datetime.now() + timedelta(days=1)
six_mo_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_mo_from_today
    )
