#!/usr/bin/python3

"""The save_to_json_file Module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON Repr.
    Args:
        my_obj: Python's object to serialize
        filename: Text file to write within
    """
    with open(filename, 'w+', encoding="utf-8") as f:
        json.dump(my_obj, f)
