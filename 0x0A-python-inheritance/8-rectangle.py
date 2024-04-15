#!/usr/bin/python3

"""The base_geometry Module"""


class BaseGeometry:
    """Class contain some geometry methods and attributes"""

    def area(self):
        """Method that raise an exception 'Exception' with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check and validate value param
        Args:
            name: name of instance
            value: value to check
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
