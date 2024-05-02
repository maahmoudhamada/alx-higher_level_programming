#!/usr/bin/python3
'''The square Module'''


class Square:
    '''The Square class'''
    def __init__(self, size=0):
        '''Constructor
        Args:
            size: Size of an square instance
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''Method to get are of a square'''
        return self.__size * self.__size
