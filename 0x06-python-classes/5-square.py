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
        """Property for size.

        Raises:
            TypeError: If Not Int.
            ValueError: If Lower Than Zero.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        """Area Function.

        Return:
            The Area of Square
        """
        return self.__size ** 2

    def my_print(self):
        """Print Square."""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()

