#!/usr/bin/python3
"""This file is creating a functin to write a text file"""


def write_file(filename="", text=""):
    """This function creates a new textfile with utf-8"""
    with open(filename, "w", encoding="utf-8", newline='') as f:
        f.write(text)
    return len(text)
