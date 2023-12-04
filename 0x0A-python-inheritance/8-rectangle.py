#!/usr/bin/python3
"""Module For A Method."""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """A Subclass That Inherits BaseGeometry Class."""

    def __init__(self, width, height):
        """Initializing A New Rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
