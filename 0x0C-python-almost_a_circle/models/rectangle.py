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

    # ========================  Str  ========================

    def __str__(self):
        """String method to print attributes"""
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

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

    # =======================  Display  =======================

    def display(self):
        """Display method"""
        shape = ""
        for i in range(self.y):
            shape += '\n'
        for h in range(self.height):
            for j in range(self.x):
                shape += ' '
            for w in range(self.width):
                shape += '#'
            shape += '\n'
        print(shape, end="")
        # return shape # for testing purpose

    # ========================  Update  ========================

    def update(self, *args, **kwargs):
        """Update method"""
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)

        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    # ========================  to_dictionary  ========================

    def to_dictionary(self):
        """Dictionary representation"""
        dic = {}
        dic.update({'id': self.id})
        dic.update({'width': self.width})
        dic.update({'height': self.height})
        dic.update({'x': self.x})
        dic.update({'y': self.y})
        return dic
