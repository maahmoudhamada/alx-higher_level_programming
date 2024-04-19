#!/usr/bin/python3

"""The 0-add_integer Module"""


def add_integer(a, b=98):
    """Return sum of two integer/floats as integer number

    Args:
        a: Integer/float number
        b: Integer/float number
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
