#!/usr/bin/python3

"""The Stduent class module"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Consturctor (Magic Method)
        Args:
            first_name: Student's first name
            last_name: Student's last name
            age: Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dict of a class - simple data structure
        for JSON serialization

        Return: Dictionary description
        """
        data = self.__dict__
        if type(attrs) is list and all(type(x) is str for x in attrs):
            new = {x: z for x, z in data.items() for y in attrs if x == y}
            return new
        else:
            return data
