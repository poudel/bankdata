import pytest
from nest_lib import nest_dicts
from tests.utils import read_json_fixture, COMMON_TEST_PARAMS


@pytest.mark.parametrize(*COMMON_TEST_PARAMS)
def test_nest_dicts(input_file, expected_output_file, nesting_keys):
    input_data = read_json_fixture(input_file)
    expected = read_json_fixture(expected_output_file)

    output = nest_dicts(input_data, nesting_keys)
    assert output == expected
