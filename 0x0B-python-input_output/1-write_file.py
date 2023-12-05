#!/usr/bin/python3
"""Input and output module."""


def write_file(filename="", text=""):
    """A function to write into file."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
