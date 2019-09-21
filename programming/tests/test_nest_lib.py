import pytest
from starlette.testclient import TestClient
from nest_lib import nest_dicts
from nest_api import app


api_client = TestClient(app)


TEST_PARAMS = [
    "input_file,expected_output_file,nesting_keys",
    [
        ("input.json", "output_currency.json", ["currency"]),
        ("input.json", "output_currency_country.json", ["currency", "country"]),
        ("input.json", "output_currency_country_city.json", ["currency", "country", "city"]),
    ],
]


@pytest.mark.parametrize(*TEST_PARAMS)
def test_nest_dicts(input_file, expected_output_file, nesting_keys, json_resource_reader):
    input_data = json_resource_reader(input_file)
    expected = json_resource_reader(expected_output_file)

    output = nest_dicts(input_data, nesting_keys)
    assert output == expected


@pytest.mark.parametrize(*TEST_PARAMS)
def test_nest_dicts_api(input_file, expected_output_file, nesting_keys, json_resource_reader):
    input_data = json_resource_reader(input_file)
    expected_response = json_resource_reader(expected_output_file)

    response = api_client.post(
        "/api/v1/nest_dicts", params={"nesting_keys": nesting_keys}, json=input_data
    )
    assert response.status_code == 200
    assert response.json() == expected_response
