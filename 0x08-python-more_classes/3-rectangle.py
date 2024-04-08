#!/usr/bin/python3
"""Module has Class 'Rectangle' that defines a rectangle"""


class Rectangle:
    """class 'Rectangle'"""

    def __init__(self, width=0, height=0):

        """init: Method called auto when creating new object
        Args:
            width: Width of a rectangle
            height: Height of a rectangle
        """

        self.height = height
        self.width = width

    def __str__(self):
        """__str__: Magic method"""
        ret = ''
        if self.width == 0 or self.height == 0:
            return ret
        for h in range(self.height):
            for w in range(self.width):
                ret += '#'
            if h != self.height - 1:
                ret += '\n'
        return ret

    def validate_width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

    def validate_height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_width(value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_height(value)
        self.__height = value

    def area(self):
        """area: Method to calculate area of a rectangle
        Return: Integer
        """
        return self.width * self.height

    def perimeter(self):
        """perimeter: Method to calculate perimeter of a rectangle
        Return: Integer
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
