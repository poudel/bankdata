from nest_lib import nest_dicts


def test_nest_dicts(input_data, expected_response, nesting_keys):
    result = nest_dicts(input_data, nesting_keys)
    assert result == expected_response
