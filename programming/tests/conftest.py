import os
import json
import pytest


RESOURCES_PATH = os.path.dirname(__file__)


def read_json(filename):
    file_path = os.path.join(RESOURCES_PATH, filename)

    with open(file_path) as file_:
        return json.load(file_)


@pytest.fixture
def input_data():
    return read_json('input.json')


@pytest.fixture
def expected_response():
    return read_json('output.json')


@pytest.fixture
def nesting_keys():
    return ['currency', 'country', 'city']
