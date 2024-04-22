#!/usr/bin/python3
"""The Square Class Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square subclass from Rectangle superclass"""

    # ========================  Init  ========================

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    # ========================  Str  ========================

    def __str__(self):
        """string method to print attributes"""
        return "[Square] ({}) {}/{} - {}" \
            .format(self.id, self.x, self.y, self.width)

    # ========================  Size  ========================

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        self.width = value
        self.height = value

    # ========================  Update  ========================

    def update(self, *args, **kwargs):
        """Update method"""
        if args:
            attributes = ['id', 'size', 'x', 'y']
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
        dic.update({'size': self.width})
        dic.update({'x': self.x})
        dic.update({'y': self.y})
        return dic
