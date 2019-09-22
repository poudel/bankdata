import sys
import json
import argparse
from nest_lib import nest_dicts


def build_args_parser():
    parser = argparse.ArgumentParser(
        description="Nest the given list of dictionaries according to the given sequence of keys"
    )
    parser.add_argument(
        "nesting_keys",
        nargs="+",
        help="Provide nesting keys in the sequence you want to nest them.",
    )

    parser.add_argument(
        "--input_data",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="Input JSON array. Can be in the form of a file path or passed through stdin",
    )

    return parser


def parse_args():
    args_parser = build_args_parser()
    args = args_parser.parse_args()

    if args.input_data.isatty():
        raise ValueError("Must provide an input JSON list.")
    return args


def main():
    try:
        args = parse_args()
        data = json.load(args.input_data)
        tree = nest_dicts(data, args.nesting_keys)
        sys.stdout.write(json.dumps(tree, indent=2))
    except Exception as err:
        sys.stderr.write("Failed to nest: \n" f"{err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
