#!/usr/bin/python3
"""Class Student Module."""


class Student:
    """Student Class."""

    def __init__(self, first_name, last_name, age):
        """Class Constructor."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation."""
        return self.__dict__
