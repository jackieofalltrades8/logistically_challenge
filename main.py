import logging

from models.Carrier import Carrier
from services.CarrierAPIClient import CarrierAPIClient

logging.basicConfig(level=logging.WARN)

if __name__ == "__main__":
    logging.debug("in main")
    api_client = CarrierAPIClient()

    # get all carriers
    carriers = api_client.get_carriers()
    logging.info(f"carriers: {carriers}")

    # get quote for each carrier
    quotes = []
    for carrier in carriers:
        carrier_quote = api_client.get_quote_for_carrier(carrier.carrier_code)
        logging.info(f"carrier quote: {carrier_quote}")
        if carrier_quote is not None: quotes.append({
            "carrier": carrier.name,
            "total_cost": carrier_quote.total_cost,
            "delivery_date": carrier_quote.delivery_date
        })

    sorted_quotes = sorted(quotes, key=lambda d: d['total_cost'], reverse=True)
    print(f"{sorted_quotes}")
