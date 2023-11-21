#!/usr/bin/python3
"""Class Module."""


class Square:
    """Defining Class."""

    def __init__(self, size=0):
        """Class Constructor

        Args:
            size: The Length of Square

        Raises:
            TypeError: if size is not integer
            ValueError: if size is lower than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area Function.
        Return:
            The Area of Square
        """
        return self.__size ** 2
