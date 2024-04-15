#!/usr/bin/python3

"""The square class module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """SubClass of the SuperClass Rectangle"""
    def __init__(self, size):
        """Constructor that builds Square class
        Args:
            size: Size of Square
        """

        super().integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Magic method to return string representation in unformal way"""
        return "[Square] {}/{}".format(self.__size, self.__size)
