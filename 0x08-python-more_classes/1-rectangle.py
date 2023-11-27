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
        """Setter for Width."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
