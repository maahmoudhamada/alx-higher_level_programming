#!/usr/bin/python3
'''The square Module'''


class Square:
    '''The Square class'''
    def size_validator(self, value):
        '''Validator for size attribute'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def pos_validator(self, value):
        '''Validator for position attribute'''
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(elem, int) and elem >= 0 for elem in value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def __init__(self, size=0, position=(0, 0)):
        '''Constructor
        Args:
            size: Size of an square instance
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Getter for size attribute'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter for size attribute'''
        self.size_validator(value)
        self.__size = value

    @property
    def position(self):
        '''Getter for position attribute'''
        return self.__position

    @position.setter
    def position(self, value):
        self.pos_validator(value)
        self.__position = value

    def area(self):
        '''Method to get are of a square'''
        return self.__size * self.__size

    def my_print(self):
        '''Method to print square using "#" char'''
        if self.size == 0:
            print()
        else:
            for ln in range(self.position[1]):
                print()
            for x in range(self.size):
                for i in range(self.position[0]):
                    print(' ', end="")
                for y in range(self.size):
                    print("#", end="")
                print()
