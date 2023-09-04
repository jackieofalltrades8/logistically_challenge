import logging

from services.CarrierAPIClient import CarrierAPIClient

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.debug("in main")
    api_client = CarrierAPIClient()
    carriers = api_client.get_carriers()
    logging.info(f"carriers: {carriers}")
    quotes = []
    for carrier in carriers:
        carrier_quote = api_client.get_quote_for_carrier(carrier["carrier_code"])
        logging.info(f"carrier quote: {carrier_quote}")
        quotes.append(carrier_quote)
    print(quotes)
    