#!/usr/bin/python3
"""Creates an Object from a Json file"""


def load_from_json_file(filename):
    """Function that creates an Object from a Json file"""
    import json
    # needs to use loads json and needs to return the input as python
    with open(filename, "r", encoding="utf-8") as js:
        content = json.load(js)
    return content
