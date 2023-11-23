#!/usr/bin/python3
"""Class Module."""


class Square:
    """Defining Class."""

    def __init__(self, size=0, position=(0, 0)):
        """Class Constructor.

        Args:
            size (int): Length of Square Side.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property for size.

        Raises:
            TypeError: If not an integer.
            ValueError: If less than zero.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get Position."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num > 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area Function.

        Returns:
            int: The Area of Square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print Square."""
        if self.__size == 0:
            print("")
            return

        for x in range(0, self.__position[1]):
            print("")

        for i in range(self.size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
        print()
