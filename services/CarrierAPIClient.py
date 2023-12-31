import logging
import requests
from constants import URL, CARRIER_ENDPOINT, RATE_ENDPOINT
from models.Carrier import Carrier
from models.Rate import Rate

class CarrierAPIClient():
    def __init__(self):
        self.url = URL
        self.carrier_endpoint = CARRIER_ENDPOINT
        self.rate_endpoint = RATE_ENDPOINT

    def get_carriers(self):
        try:
            response = requests.get(f"{self.url}{self.carrier_endpoint}")
            carriers = response.json()["carriers"]
            carrier_list = [
                Carrier(**carrier) for carrier in carriers
            ]
            return carrier_list
        except Exception:
            return None

    def get_quote_for_carrier(self, carrier_code):
        try:
            response = requests.get(f"{self.url}{self.rate_endpoint}/{carrier_code}", timeout=8)
            response_json = response.json()
            if "error_message" in response_json:
                raise Exception(response_json)
            return Rate(**response_json)
        except Exception as e:
            logging.error(f"An error occurred getting quote for {carrier_code}: {e}")
            return None
