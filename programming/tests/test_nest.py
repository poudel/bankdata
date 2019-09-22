import os
import json
import pytest
import pexpect
from nest import build_args_parser
from tests.utils import PROJECT_DIR, FIXTURES_DIR, COMMON_TEST_PARAMS, read_json_fixture


def test_build_args_parser():
    parser = build_args_parser()

    # asserts that
    with pytest.raises(SystemExit):
        parser.parse_args()

    nesting_keys = ["a", "b", "c"]
    args = parser.parse_args(nesting_keys)
    assert args.nesting_keys == nesting_keys


@pytest.mark.parametrize(*COMMON_TEST_PARAMS)
def test_main(input_file, expected_output_file, nesting_keys):
    expected = read_json_fixture(expected_output_file)

    input_file_path = os.path.join(FIXTURES_DIR, input_file)
    script_path = os.path.join(PROJECT_DIR, "nest.py")

    nesting_keys_joined = " ".join(nesting_keys)
    command = f"cat {input_file_path} | python {script_path} {nesting_keys_joined}"

    child = pexpect.spawn("/bin/bash", ["-c", command])

    output = json.loads(child.read())

    assert output == expected
