# -*- coding: utf-8 -*-
import json

if __name__ == '__main__':
    a_map = {
        1: {
            "id": 1,
            "parent_id": 0
        },
        2: {
            "id": 2,
            "parent_id": 1
        },
        3: {
            "id": 3,
            "parent_id": 2
        }
    }

    tree_map = {

    }

    for key in a_map:
        parent_id = a_map[key]['parent_id']
        if parent_id in a_map:
            if "child" not in a_map[parent_id]:
                a_map[parent_id]["child"] = []
            a_map[parent_id]["child"].append(a_map[key])
            pass
        else:
            tree_map[parent_id] = a_map[key]

    print json.dumps(tree_map)
