#!/usr/bin/python3
"""Module For A Method."""
Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """A Class That Inherits BaseGeometry Class."""

    def __init__(self, size):
        """Initializing A New Rectangle.

        Args:
            size (int): The Size of each Side.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns The Area of The Rectangle."""
        return self.__size ** 2
