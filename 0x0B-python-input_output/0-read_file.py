#!/usr/bin/python3
"""Input and output module."""


def read_file(filename=""):
    """Reading filename with utf-8 encoding."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
