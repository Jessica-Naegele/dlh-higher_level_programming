#!/usr/bin/env python3
"""
    module defines a module for serialization and
    deserialization of json files
"""


def serialize_and_save_to_file(data, filename):
    """
        Module serialize and save data to a specific
        json file
        data: A Python Dictionary with data
        filename: The filename of the output JSON file.
            If the output file already exists it should be replaced.
    """
    import json
    with open(filename, "w", encoding="utf-8") as js:
        json.dump(data, js)
    pass


def load_and_deserialize(filename):
    """
        Module loads and deserialize data from the
        specified file
        filename: input json file. function returns a Python Dictionary
    """
    import json
    with open(filename, "r", encoding="utf-8") as js:
        content = json.load(js)
    return content
    pass
