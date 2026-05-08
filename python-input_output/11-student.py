#!/usr/bin/python3
"""Create a class Student"""


class Student:
    """Class defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a student instance"""
        if attrs is None:
            value = self.__dict__
        else:
            value = {
                key: self.__dict__[key]
                for key in attrs if key in self.__dict__
            }
        return value

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
