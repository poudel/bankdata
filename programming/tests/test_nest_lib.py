import pytest
from nest_lib import nest_dicts, validate_item, validate_nesting_keys
from tests.utils import read_json_fixture, COMMON_TEST_PARAMS


@pytest.mark.parametrize(*COMMON_TEST_PARAMS)
def test_nest_dicts(input_file, expected_output_file, nesting_keys):
    input_data = read_json_fixture(input_file)
    expected = read_json_fixture(expected_output_file)

    output = nest_dicts(input_data, nesting_keys)
    assert output == expected


def test_validate_item():
    input_data = read_json_fixture("input.json")
    item = input_data[0]

    # asserts that exception is not raised for valid keys
    nesting_keys = {"currency", "city"}
    validate_item(item, nesting_keys)

    # asserts that exception is raised for invalid keys
    invalid_nesting_keys = {"garbage_key"}
    with pytest.raises(ValueError) as execinfo:
        validate_item(item, invalid_nesting_keys)

    assert (
        f"Nesting key(s): {invalid_nesting_keys} doesn't exist inside item: {item}"
        in str(execinfo.value)
    )


def test_validate_nesting_keys():
    nesting_keys = ["currency", "city", "currency"]

    with pytest.raises(ValueError) as execinfo:
        validate_nesting_keys(nesting_keys)

    assert f"Given nesting scheme contain duplicate keys: {nesting_keys}" in str(
        execinfo.value
    )
