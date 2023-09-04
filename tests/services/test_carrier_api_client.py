import unittest
from unittest.mock import MagicMock, patch
from tests.data.test_carrier_list import carrier_list

from services.CarrierAPIClient import CarrierAPIClient

class TestCarrierAPIClient(unittest.TestCase):

    @patch('requests.get')
    def test_get_carriers_success(self, mock_get):
        # Mock requests.get 
        mock_response = MagicMock()
        mock_response.json.return_value = carrier_list
        mock_get.return_value = mock_response

        client = CarrierAPIClient()
        carriers = client.get_carriers()

        self.assertEqual(len(carriers), 2)
        self.assertEqual(carriers[0].name, "ABF Freight")
        self.assertEqual(carriers[1].name, "XPO Logistics")

    @patch('requests.get')
    def test_get_carriers_failure(self, mock_get):
        # Mock requests.get to simulate an exception
        mock_get.side_effect = Exception("Something went wrong")

        client = CarrierAPIClient()
        carriers = client.get_carriers()

        self.assertIsNone(carriers)
