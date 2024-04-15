#!/usr/bin/python3

"""The base_geometry Module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass 'Rectangle' inherted from superClass BaseGeometry"""

    def __init__(self, width, height):
        """Constructor magic method
        Args:
            width: Width of rectangle
            height: Height of rectangle
        """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return string representation"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Return area of a rectangle <width>*<height>"""
        return self.__width * self.__height
