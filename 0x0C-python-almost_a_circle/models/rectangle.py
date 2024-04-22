#!/usr/bin/python3
"""The Rectangle Class Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def validator(self, name, value):
        """Validtor for entered values"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0 and (name == 'width' or name == 'height'):
            raise ValueError("{} must be > 0".format(name))
        elif value < 0 and (name == 'x' or name == 'y'):
            raise ValueError("{} must be >= 0".format(name))

    # ========================  Init  ========================

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # ========================  Width  ========================

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        self.validator('width', value)
        self.__width = value

    # ========================  Height  ========================

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.validator('height', value)
        self.__height = value

    # ========================  X  ========================

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.validator('x', value)
        self.__x = value

    # ========================  Y  ========================

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.validator('y', value)
        self.__y = value

    # ========================  Area  ========================

    def area(self):
        """area method"""
        return self.width * self.height
