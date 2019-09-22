import os
import json
import pytest
import pexpect
from tests.utils import PROJECT_DIR, FIXTURES_DIR, COMMON_TEST_PARAMS, read_json_fixture


SCRIPT_PATH = os.path.join(PROJECT_DIR, "nest.py")


def pexpect_spawn_nest_script(fixture_filename, nesting_keys):
    input_file_path = os.path.join(FIXTURES_DIR, fixture_filename)
    nesting_keys_joined = " ".join(nesting_keys)
    command = f"cat {input_file_path} | python {SCRIPT_PATH} {nesting_keys_joined}"

    shell = os.environ["SHELL"]
    return pexpect.spawn(shell, ["-c", command])


@pytest.mark.parametrize(*COMMON_TEST_PARAMS)
def test_main(input_file, expected_output_file, nesting_keys):
    expected = read_json_fixture(expected_output_file)

    child = pexpect_spawn_nest_script(input_file, nesting_keys)
    output = json.loads(child.read())

    assert output == expected


def test_main_without_nesting_keys():
    child = pexpect_spawn_nest_script("input.json", [])
    child.expect("nest.py: error: the following arguments are required: nesting_keys")


def test_main_without_input():
    command = f"python {SCRIPT_PATH} some_key"
    child = pexpect.spawn(command)
    child.expect("Must provide an input JSON list.")


def test_main_with_invalid_input():
    child = pexpect_spawn_nest_script("invalid_input.json", ["country"])
    child.expect("Failed to nest: ")
