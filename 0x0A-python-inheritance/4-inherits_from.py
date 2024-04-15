#!/usr/bin/python3

"""The inherits_from module"""


def inherits_from(obj, a_class):
    """Return true if obj is instance of a_class and not equal to a_class
    false otherwise

    Args:
        obj: Object
        a_class: Class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
