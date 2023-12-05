#!/usr/bin/python3
"""Input and output module."""
import json


def from_json_string(my_str):
    """A function to get an object from json."""
    return json.loads(my_str)
