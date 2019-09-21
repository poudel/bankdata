#!/user/bin/env python

import sys
import logging


def nest_it(items, nesting_keys):
    leaf_nesting_key = nesting_keys[-1]
    big_tree = {}

    for item in items:
        tree = big_tree

        # items in the leaf node list are always going to be:
        # (original item without the keys in nesting_keys)
        leaf_item = {
            k: v for k, v in item.items()
            if k not in nesting_keys
        }

        for nesting_key in nesting_keys:
            next_node_key = item[nesting_key]

            if next_node_key not in tree:
                is_leaf = nesting_key == leaf_nesting_key
                tree[next_node_key] = [] if is_leaf else {}

            tree = tree[next_node_key]

        # in the end, the `tree` is always
        # going to be the leaf node
        tree.append(leaf_item)

    return big_tree
