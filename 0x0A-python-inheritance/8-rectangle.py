#!/usr/bin/python3
"""Module For A Method."""

BaseGeometry = __import__("7-base_geometry.py").BaseGeometry


class Rectangle(BaseGeometry):
    """A Class That Inherits BaseGeometry Class."""

    def __init__(self, width, height):
        """Initializing A New Rectangle.

        Args:
            width: The Width.
            height: The Height.
        """
        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height
