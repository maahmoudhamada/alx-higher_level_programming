#!/usr/bin/python3

"""The class_to_json Module"""


def class_to_json(obj):
    """Return dict of a class - simple data structure for JSON serialization
    Args:
        obj: Instance of a specific class
    Return: Dictionary description
    """
    return obj.__dict__
