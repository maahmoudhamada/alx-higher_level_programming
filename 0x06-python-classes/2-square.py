#!/usr/bin/python3


"""Module containg class 'Square'"""


class Square:
    """Square: a Class"""

    def __init__(self, size=0):
        """
        __init__: Constructor for 'Square' class
        Args:
            size (int): Size of square
        Return:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
