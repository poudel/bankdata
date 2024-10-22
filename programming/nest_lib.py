"""
Given a flat list of dictionaries, return a nested dictionary
according to the provided nesting keys.
"""


def validate_item(item, nesting_keys):
    nesting_keys = set(nesting_keys)

    difference = nesting_keys.difference(item.keys())

    if difference:
        raise ValueError(
            f"Nesting key(s): {difference} doesn't exist inside item: {item}."
        )


def validate_nesting_keys(nesting_keys):
    if len(nesting_keys) != len(set(nesting_keys)):
        raise ValueError(f"Given nesting scheme contain duplicate keys: {nesting_keys}")


def nest_dicts(items, nesting_keys):
    validate_nesting_keys(nesting_keys)
    big_tree = {}

    for item in items:
        validate_item(item, nesting_keys)

        tree = big_tree

        # items in the leaf node list are always going to be:
        # (original item without the keys in nesting_keys)
        leaf_item = {k: v for k, v in item.items() if k not in nesting_keys}

        for nesting_key in nesting_keys:
            next_node_key = item[nesting_key]

            # The input/output are usually json. JSON standard
            # requires that the keys always be strings. Let us
            # explicitly cast the keys to strings even though
            # json.dumps can do that implicitly.
            if not isinstance(next_node_key, str):
                next_node_key = str(next_node_key)

            if next_node_key not in tree:
                is_leaf = nesting_key == nesting_keys[-1]
                tree[next_node_key] = [] if is_leaf else {}

            tree = tree[next_node_key]

        # `tree` is always going to be the leaf node
        # but `leaf_item` can be an empty dict
        if leaf_item:
            tree.append(leaf_item)

    return big_tree
