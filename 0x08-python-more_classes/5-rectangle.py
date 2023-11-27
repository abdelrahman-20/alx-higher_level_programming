#!/usr/bin/python3
"""Rectangle Module."""


class Rectangle:
    """This is Class."""

    def __init__(self, width=0, height=0):
        """Initializing Dimensions."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for Width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for Width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for Height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for Setter."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A Function To Get Area."""
        return self.__width * self.__height

    def perimeter(self):
        """A Function To Get Perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Print The Rectangle with Hashes."""
        output = ""
        if self.__width != 0 and self.__height != 0:
            output += "\n".join("#" * self.__width
                                for _ in range(self.__height))
        return output

    def __repr__(self):
        """Returns A Representation of Class."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Returns A Message when Deleted."""
        print("Bye rectangle...")
