#!/usr/bin/python3
"""Module for a class."""


class MyList(list):
    """A subclass representing list class."""
    def print_sort(self):
        """A function to print sorted list"""
        print(sorted(self))
