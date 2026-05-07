#!/usr/bin/python3
"""creation of a class student"""


class Student:
    """class defining students"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function retunrs a dictionary """
        values = self.__dict__
        return values
