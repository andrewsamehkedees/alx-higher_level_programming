#!/usr/bin/python3
import sys

# Import the required functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Try to load the list from the file, or create a new list if the file doesn't exist
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

# Add all command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the list back to the file
save_to_json_file(my_list, filename)
