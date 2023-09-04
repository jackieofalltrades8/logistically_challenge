import requests
from constants import URL, CARRIER_ENDPOINT

class CarrierAPIClient():
    def __init__(self):
        self.url = URL
        self.carrier_endpoint = CARRIER_ENDPOINT

    def get_carriers(self):
        try:
            response = requests.get(f"{self.url}{self.carrier_endpoint}")
            return response.json()["carriers"]
        except Exception:
            return None