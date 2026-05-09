#!/usr/bin/python3
"""Module inserts a line of text to a file, after each lin containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Function inserts a new_string after search_string in filename"""
    with open(filename, "a", encoding="utf-8") as f:
        if search_string in line:
            f.write(new_string)
