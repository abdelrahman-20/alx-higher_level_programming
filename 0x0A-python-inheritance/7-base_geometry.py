#!/usr/bin/python3
"""Module For A Method."""


class BaseGeometry:
    """This is Empty Class."""
    def area(self):
        """A Function To Get The Area and Not Implemented Yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A Function To Validate The value

        Args:
            name: The Name.
            value: The Value to Check.

        Raises:
            TypeError: if value is not integer.
            ValueError: if value is less than or equal 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
