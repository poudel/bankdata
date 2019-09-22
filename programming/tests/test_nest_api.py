import base64
import pytest
from starlette.testclient import TestClient
from nest_api import app, USERNAME, PASSWORD
from tests.utils import read_json_fixture, COMMON_TEST_PARAMS


api_client = TestClient(app)


def get_basicauth_headers():
    credential = f"{USERNAME}:{PASSWORD}"
    credential_b64 = base64.b64encode(credential.encode()).decode()
    header = {"Authorization": f"Basic {credential_b64}"}
    return header


@pytest.mark.parametrize(*COMMON_TEST_PARAMS)
def test_nest_dicts_api(input_file, expected_output_file, nesting_keys):
    input_data = read_json_fixture(input_file)
    expected_response = read_json_fixture(expected_output_file)

    response = api_client.post(
        "/api/v1/nest_dicts",
        params={"nesting_keys": nesting_keys},
        json=input_data,
        headers=get_basicauth_headers(),
    )
    assert response.status_code == 200
    assert response.json() == expected_response
