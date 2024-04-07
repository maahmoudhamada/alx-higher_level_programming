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

    def area(self):
        """area: Public instance method
        Return: Area of a square (int)
        """
        return pow(self.__size, 2)

    @property
    def size(self):
        """size: Getter method
        Return: current instance attribute 'size'
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size: Setter method
        Args:
            value: Value of square's size to be setted
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
