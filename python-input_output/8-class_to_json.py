#!/usr/bin/python3
"""this modules returns a dictionary for JSON serialisation"""


def class_to_json(obj):
    """Function retunrs a dictionary """
    values = obj.__dict__
    return values
