#!/usr/bin/python3

"""The is_kind_of_class Module"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a class inherted from

    Args:
        obj: Object
        a_class: Class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
