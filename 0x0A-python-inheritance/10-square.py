#!/usr/bin/python3
"""Module For A Method."""
Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """A class that represents a square."""

    def __init__(self, size):
        """Constructor."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method for area of square."""
        return self.__size ** 2
