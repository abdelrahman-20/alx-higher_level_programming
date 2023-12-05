#!/usr/bin/python3
"""Input and output module."""
import json


def load_from_json_file(filename):
    """A function to create object from json file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
