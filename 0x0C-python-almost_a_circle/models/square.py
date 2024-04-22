#!/usr/bin/python3
"""The Square Class Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square subclass from Rectangle superclass"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string method to print attributes"""
        return "[Square] ({}) {}/{} - {}" \
            .format(self.id, self.x, self.y, self.width)
