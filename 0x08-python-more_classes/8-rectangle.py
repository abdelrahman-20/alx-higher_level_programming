#!/usr/bin/python3
"""Rectangle Module."""


class Rectangle:
    """This is Rectangle Class."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing Dimensions."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Print The Rectangle with Hashes.

        Returns:
            A Rectangle with Specific Character.
        """
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """Returns A Representation of Class."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Returns A Message when Deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """A Function That Returns The Bigger Instance in Area.

        Args:
            rect_1: First Instance.
            rect_2: Second Instance.

        Raises:
            TypeError: if one of the 2 args is not Rectangle.
        Returns:
            The Instance with Larger Area.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
