#!/usr/bin/python3
import sys
import json
"""function save"""

def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))

"""function load"""
def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

filename = "add_item.json"
if os.path.isfile(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)

