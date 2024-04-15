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
