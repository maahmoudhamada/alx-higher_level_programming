#!/usr/bin/python3

"""The load_from_json_file Module"""
import json


def load_from_json_file(filename):
    """Convert JSON string to python object from a file (deserialization)
    Args:
        filename: Text file contain JSON String
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data
