#!/usr/bin/python3
"""Input and output module."""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__(
        "6-load_from_json_file").load_from_json_file

    try:
        old_data = load_from_json_file('add_item.json')
    except Exception:
        old_data = []

    old_data.extend.extend(sys.argv[1:])
    save_to_json_file(old_data, "add_item.json")

