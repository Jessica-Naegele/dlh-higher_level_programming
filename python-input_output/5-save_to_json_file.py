#!/usr/bin/python3
"""Module saves string into json file"""


def save_to_json_file(my_obj, filename):
    """Function creates a json file and saves str"""
    import json
    # json.dumps needs to  be used
    text = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as js:
        js.write(text)
