#!/usr/bin/python3

"""The write_file module"""


def write_file(filename="", text=""):
    """Write into an object's stream (file)
    Args:
        filename: Name of file to open
        text: Content to be writtern into a file
    Return:
        Number of character written to the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        charNum = f.write(text)
    return charNum
