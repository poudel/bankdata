from unittest import TestCase
from nest_lib import nest_dicts


INPUT_DATA = [
    {
        "country": "US",
        "city": "Boston",
        "currency": "USD",
        "amount": 100
    },
    {
        "country": "FR",
        "city": "Paris",
        "currency": "EUR",
        "amount": 20
    },
    {
        "country": "FR",
        "city": "Lyon",
        "currency": "EUR",
        "amount": 11.4
    },
    {
        "country": "ES",
        "city": "Madrid",
        "currency": "EUR",
        "amount": 8.9
    },
    {
        "country": "UK",
        "city": "London",
        "currency": "GBP",
        "amount": 12.2
    },
    {
        "country": "UK",
        "city": "London",
        "currency": "FBP",
        "amount": 10.9
    }
]


EXPECTED_RESPONSE = {
    "EUR": {
        "ES": {
            "Madrid": [
                {
                    "amount": 8.9
                }
            ]
        },
        "FR": {
            "Lyon": [
                {
                    "amount": 11.4
                }
            ],
            "Paris": [
                {
                    "amount": 20
                }
            ]
        }
    },
    "FBP": {
        "UK": {
            "London": [
                {
                    "amount": 10.9
                }
            ]
        }
    },
    "GBP": {
        "UK": {
            "London": [
                {
                    "amount": 12.2
                }
            ]
        }
    },
    "USD": {
        "US": {
            "Boston": [
                {
                    "amount": 100
                }
            ]
        }
    }
}


class TestNest(TestCase):

    def test_nest_dicts(self):
        result = nest_dicts(INPUT_DATA, ['currency', 'country', 'city'])
        self.assertEqual(result, EXPECTED_RESPONSE)
