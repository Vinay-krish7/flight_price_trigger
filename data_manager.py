import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import pprint

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/5f613009b8f647691711810bfcd4e88e/flightDeals/prices"


class DataManager:

    def __init__(self):
        # self._user = os.environ["SHEETY_USERNAME"]
        # self._password = os.environ["SHEETY_PASSWORD"]
        # self._token = os.environ["SHEETY_TOKEN"]
        self._headers = {
            "Authorization":"Basic dmluYXk6c2Jjd2Vjd2VnZzZm="
        }
        # self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):

        try:
            response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers = self._headers)

            data = response.json()

            self.destination_data = data["prices"]

            return self.destination_data
        except Exception as e:
            print(f"Error during data fetch{e}")

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers = self._headers
            )
            # print(response.text)
