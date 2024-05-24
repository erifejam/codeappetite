import unittest
from unittest.mock import patch
from geolocationService.geolocation import match_locations

class GeolocationTestCase(unittest.TestCase):
    @patch('geolocationService.geolocation.client')
    def test_match_locations(self, mock_client):
        mock_client.search_place_index_for_position.return_value = {
            'Results': [
                {'Place': {'Label': 'User Location 1'}},
                {'Place': {'Label': 'User Location 2'}},
                {'Place': {'Label': 'User Location 3'}},
            ]
        }

        location = (37.7749, -122.4194)  # San Francisco coordinates
        nearby_locations = match_locations(location)

        self.assertEqual(nearby_locations, ['User Location 1', 'User Location 2', 'User Location 3'])

if __name__ == '__main__':
    unittest.main()
