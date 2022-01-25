from dotenv import load_dotenv
import os
import requests

load_dotenv()

# NOTE: User's will need their own environmental data.
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
SHEETY_URL = os.getenv("SHEETY_URL")

HEADERS = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_URL, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self, id, iata):
        new_data = {
            "price": {
                "iataCode": iata
            }
        }
        response = requests.put(url=f"{SHEETY_URL}/{id}", json=new_data, headers=HEADERS)
        return response.json()
