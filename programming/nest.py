import sys
import json
from nest_lib import nest_dicts


def parse_sys_args():
    if len(sys.argv) < 2:
        sys.stderr.write('Please provide space separated nesting keys..')
    return sys.argv[1:]


def main():
    nesting_keys = parse_sys_args()
    data = json.load(sys.stdin)
    tree = nest_dicts(data, nesting_keys)
    sys.stdout.write(json.dumps(tree, indent=4))


if __name__ == "__main__":
    main()
