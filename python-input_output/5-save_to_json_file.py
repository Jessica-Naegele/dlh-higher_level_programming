#!/usr/bin/python3
"""Module creates a function returning a JSON string"""


def save_to_json_file(my_obj, filename):
    """Function creates a json file and saves str"""
    import json
    # json.dump needs to  be used)
    with open(filename, "w", encoding="utf-8") as js:
        json.dump(my_obj, js)
