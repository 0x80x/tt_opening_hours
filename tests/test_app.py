import os
import sys
# "Костыль" для добавления путей в PYTHONPATH, иначе импорты app ломаются
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")))

from app.api import app
from fastapi.testclient import TestClient
import unittest



class TestOpeningHoursEndpoint(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.client = TestClient(app)

    def test_opening_hours_endpoint(self):
        opening_hours = {
            "tuesday": [
                {
                    "type": "open",
                    "value": 36000
                },
                {
                    "type": "close",
                    "value": 64800
                }
            ],
            "thursday": [
                {
                    "type": "open",
                    "value": 37800
                },
                {
                    "type": "close",
                    "value": 64800
                }
            ],
            "friday": [
                {
                    "type": "open",
                    "value": 36000
                }
            ],
            "saturday": [
                {
                    "type": "close",
                    "value": 3600
                },
                {
                    "type": "open",
                    "value": 36000
                }
            ],
            "sunday": [
                {
                    "type": "close",
                    "value": 3600
                },
                {
                    "type": "open",
                    "value": 43200
                },
                {
                    "type": "close",
                    "value": 75600
                }
            ]
        }

        result_text =  "Monday: Closed\nTuesday: 10:00 AM - 6:00 PM\nWednesday: Closed\nThursday: 10:30 AM - 6:00 PM\nFriday: 10:00 AM - 1:00 AM\nSaturday: 10:00 AM - 1:00 AM\nSunday: 0:00 PM - 9:00 PM"

        response = self.client.post("/opening-hours", json=opening_hours)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), result_text)


if __name__ == "__main__":
    unittest.main()
