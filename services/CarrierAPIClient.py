import logging
import requests
from constants import URL, CARRIER_ENDPOINT, RATE_ENDPOINT

class CarrierAPIClient():
    def __init__(self):
        self.url = URL
        self.carrier_endpoint = CARRIER_ENDPOINT
        self.rate_endpoint = RATE_ENDPOINT

    def get_carriers(self):
        try:
            response = requests.get(f"{self.url}{self.carrier_endpoint}")
            return response.json()["carriers"]
        except Exception:
            return None

    def get_quote_for_carrier(self, carrier_code):
        try:
            response = requests.get(f"{self.url}{self.rate_endpoint}/{carrier_code}")
            response_json = response.json()
            if "error_message" in response_json:
                raise Exception
            return response_json
        except Exception:
            logging.error(f"An error occurred getting quote for {carrier_code}: {response_json}")
            return None
