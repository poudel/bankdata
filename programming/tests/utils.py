import os
import json


TESTS_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.dirname(TESTS_DIR)
FIXTURES_DIR = os.path.join(TESTS_DIR, 'fixtures')


COMMON_TEST_PARAMS = [
    "input_file,expected_output_file,nesting_keys",
    [
        ("input.json", "output_currency.json", ["currency"]),
        ("input.json", "output_currency_country.json", ["currency", "country"]),
        ("input.json", "output_currency_country_city.json", ["currency", "country", "city"]),
        ("input.json", "output_currency_country_city_amount.json", ["currency", "country", "city", "amount"]),
    ],
]


def read_json_fixture(filename):
    file_path = os.path.join(FIXTURES_DIR, filename)

    with open(file_path) as file_:
        return json.load(file_)
