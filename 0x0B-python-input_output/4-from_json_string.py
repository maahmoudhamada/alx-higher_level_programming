#!/usr/bin/python3

"""The from_json_string Module"""
import json


def from_json_string(my_str):
    """Convert (deserialization) json string to python object
    Args:
        my_str: String to deserialize
    Return:
        Python Object data
    """
    return json.loads(my_str)
