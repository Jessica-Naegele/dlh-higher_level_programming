#!/usr/bin/python3
"""This module returns a JSON in a string"""


def to_json_string(my_obj):
    """This function returns a json in a string"""
    import json
    te = str(json.dumps(my_obj))
    return te
