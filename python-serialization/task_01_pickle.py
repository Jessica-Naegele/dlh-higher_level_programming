#!/usr/bin/env python3
"""Module creates a class CustomObject"""

import pickle
import os


class CustomObject:
    """
        Class with the attributes name(str), age(int), is_student
        (boolean) and the methods display, serialize, deserialize
    """

    def __init__(self, name, age, is_student):
        """Initialising the class with name, age and is_student"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Class metod pring object's attribute in a fixed format"""
        print(
            "Name: {} \n Age: {} \n Is Student: {}".
            format(self.name, self.age, self.is_student)
            )

    def serialize(self, filename):
        """
            Method using pickle method to take privded object and
            save it to filename
        """
        with open(filename, "wb") as pc:
            pickle.dump(self, pc)

    @classmethod
    def deserialize(cls, filename):
        """
            Method will take a filename Using the pickle module,
            it will load and return an instance of he CustomObject
            from provided filename
        """
        try:
            with open(filename, "rb") as pc:
                data = pickle.load(pc)
            return data
            cls.display(data)
        except (pickle.UnpicklingError, FileNotFoundError, EOFError):
            return None
