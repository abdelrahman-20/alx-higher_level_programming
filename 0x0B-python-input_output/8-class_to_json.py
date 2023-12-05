#!/usr/bin/python3
"""Input and output module."""


def class_to_json(obj):
    """Returns a dictionary for class object."""
    return obj.__dict__
