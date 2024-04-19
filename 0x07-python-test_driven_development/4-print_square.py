#!/usr/bin/python3

"""The print_square module

Function:
    print_square
"""


def print_square(size):
    """Function to print square composed of `#` char
    Args:
        size: Size of square (integer)
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for x in range(size):
            for y in range(size):
                print('#', end="")
            print()
