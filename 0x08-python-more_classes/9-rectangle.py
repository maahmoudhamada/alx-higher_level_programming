#!/usr/bin/python3
"""Module has Class 'Rectangle' that defines a rectangle"""


class Rectangle:
    """class 'Rectangle'"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """init: Method called auto when creating new object
        Args:
            width: Width of a rectangle
            height: Height of a rectangle
        """

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """__str__: This is used to find the informal (or nicely printable)
        string representation of an object. It's meant to be human-readable."""
        ret = ''
        if self.width == 0 or self.height == 0:
            return ret
        for h in range(self.height):
            for w in range(self.width):
                ret += str(self.print_symbol)
            if h != self.height - 1:
                ret += '\n'
        return ret

    def __repr__(self):
        """__repr__: This is used to find the official string representation
        of an object. This one is meant to be unambiguous and,
        if possible, should allow the object to be reproduced
        exactly based on its string representation.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """__del__: Magic Method to delete instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if rect_1.__class__ is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif rect_2.__class__ is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Square: Class method to init a new instance within class
        Args:
            cls: Equivalent to self but for classmethod
            size: Size of Square (Size == width == height)
        """
        return Rectangle(size, size)
