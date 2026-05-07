#!/usr/bin/python3
"""This module defines a function writing or appending a text file"""


def append_write(filename="", text=""):
    """This function writes or appends a text file by text"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
