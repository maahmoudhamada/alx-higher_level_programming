#!/usr/bin/python3

"""The is_same_class Module"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of class a_class

    Args:
        obj: Object
        a_class: Class
    """
    if isinstance(obj, a_class) and type(obj).__name__ == a_class.__name__:
        return True
    else:
        return False
