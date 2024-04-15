#!/usr/bin/python3

"""The lookup module contain lookup function"""

def lookup(obj):
    """Return available attributes and methods of an object

    Args:
        obj: object to looking into it
    """
    return list(dir(obj))