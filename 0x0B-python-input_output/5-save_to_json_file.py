#!/usr/bin/python3
"""Input and output module."""
import json


def save_to_json_file(my_obj, filename):
    """A function to write object to json file."""
    with open(filename, "a", encoding="utf-8") as file:
        json.dump(my_obj, file)
