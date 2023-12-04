# !/usr/bin/python3
"""Module For Rectangle Class."""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass representing rectangle."""

    def __init__(self, width, height):
        """Constructor."""
        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height

    def area(self):
        """Returns The Area of The Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Print in Specific Way."""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
