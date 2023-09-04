import os
from dotenv import load_dotenv
load_dotenv()

URL = os.getenv("URL")
CARRIER_ENDPOINT = os.getenv("CARRIER_ENDPOINT")