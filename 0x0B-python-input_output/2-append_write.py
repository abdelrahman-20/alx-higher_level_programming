#!/usr/bin/python3
"""Input and output module."""


def append_write(filename="", text=""):
    """A function to write into file."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
