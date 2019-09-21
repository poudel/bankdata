import os
import json
import pytest


RESOURCES_PATH = os.path.join(os.path.dirname(__file__), 'resources')


def read_json(filename):
    file_path = os.path.join(RESOURCES_PATH, filename)

    with open(file_path) as file_:
        return json.load(file_)


@pytest.fixture
def json_resource_reader():
    return read_json
