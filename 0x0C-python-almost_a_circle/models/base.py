#!/usr/bin/python3
"""The Base class Module"""
import json


class Base:
    """Base Class"""

    __nb_objects = 0

    # ========================  Init  ========================

    def __init__(self, id=None):
        """Constructor method to build base class
        Args:
            id: Unique number
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # ========================  to_json_string  ========================

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON representation"""
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    # ========================  save_to_file  ========================

    @classmethod
    def save_to_file(cls, list_objs):
        """save JSON strings into class files"""
        if list_objs is not None:
            final_lst = [x.to_dictionary() for x in list_objs]
            with open("{}.json".format(cls.__name__), 'w+', encoding="utf-8") as f:
                f.write(cls.to_json_string(final_lst))
