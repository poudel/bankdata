from starlette.testclient import TestClient

from nest_api import app

client = TestClient(app)


def test_nest_dicts_api(input_data, expected_response, nesting_keys):
    response = client.post(
        "/api/v1/nest_dicts", params={"nesting_keys": nesting_keys}, json=input_data
    )
    assert response.status_code == 200
    assert response.json() == expected_response
