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
        """ Property for size.

        Returns:
            The Size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ A Setter Property

        Raises:
            TypeError: If Not Int
            ValueError: If Lower Than Zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """A Function To Get Area of Square.

        Returns:
            The Size Square.
        """
        return self.__size ** 2

