#!/usr/bin/python3
"""Module creates a function returning a JSON string"""


def from_json_string(my_str):
    """Function returns a represenation of a JSON string"""
    import json  # json converter
    return json.loads(my_str)
