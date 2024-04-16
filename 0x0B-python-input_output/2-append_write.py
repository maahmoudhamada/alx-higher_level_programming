#!/usr/bin/python3

"""The append_write Module"""


def append_write(filename="", text=""):
    """append text to file wether file exists or not
    Args:
        filename: Name of the file
        text: Text to append

    Return:
        Number of character appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        charNum = f.write(text)
    return charNum
