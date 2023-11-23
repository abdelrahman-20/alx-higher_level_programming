#!/usr/bin/python3
"""Class Module."""


class Square:
    """Defining Class."""

    def __init__(self, size=0):
        """Class Constructor.
        
        Args:
            size: Length of Square Side.
        """
        self.size = size

    @property
    def size(self):
        """ Property for size."""
        return self.size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    def area(self):
        """A Function To Get Area of Square.

        Return:
            The Size Square.
        """
        return self.size ** 2

