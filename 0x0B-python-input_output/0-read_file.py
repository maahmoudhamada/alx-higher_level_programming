#!/usr/bin/python3

"""The read_file module"""


def read_file(filename=""):
    """Read a object's stream (file)
    Args:
        filename: Name of the file to read
    """

    with open(filename, 'r', encoding="utf-8") as f:
        for lines in f:
            print("{}".format(lines), end="")
