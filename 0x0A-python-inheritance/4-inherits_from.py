#!/usr/bin/python3

"""The inherits_from Module"""


def inherits_from(obj, a_class):
    try:
        isinstance(obj, a_class)
        issubclass(type(obj).__name__, a_class.__name__)
    except TypeError:
        return False
    else:
        return True