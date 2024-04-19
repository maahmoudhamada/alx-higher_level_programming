#!/usr/bin/python3

"""The say_my_name Module
Functions:
    say_my_name
"""


def say_my_name(first_name, last_name=""):
    """Compose and print a sentence using 2 params
    Args:
        first_name: String
        last_name: String
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
