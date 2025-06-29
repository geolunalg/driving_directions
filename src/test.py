import unittest
from api import get_address_coordinates, get_directions


class TestAPI(unittest.TestCase):
    def test_get_coordinates_valid(self):
        address = '1000 Vin Scully Avenue Los Angeles, CA 90012'
        expected = (34.073563, -118.240479)
        result = get_address_coordinates(address)
        self.assertEqual(expected, result)

    def test_get_coordinates_empty(self):
        address = ''
        expected = 'ERROR: address connot be empty'
        result = get_address_coordinates(address)
        self.assertEqual(expected, result)

    def test_get_coordinates_invalid(self):
        address = 'XXXXXXXXXX XXXXXXXXXXXXXX'
        expected = 'ERROR:'
        result = get_address_coordinates(address)
        self.assertIn(expected, result)

    def test_get_directions_invalid(self):
        # valid latitude value must be between -90 and 90
        # valid longitude value must be between -180 and 180
        src = (95.0677056, -200.2520088)
        dst = (34.073563, -118.240479)
        results = get_directions(src, dst)
        self.assertEqual(len(results), 1)
        self.assertIn('ERROR:', results[0])
