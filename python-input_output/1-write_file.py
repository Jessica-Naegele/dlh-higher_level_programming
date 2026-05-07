#!/usr/bin/python3
"""This file is creating a functin to write a text file"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
