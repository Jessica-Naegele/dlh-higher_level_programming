#!/usr/bin/python3
""" Create a module to read a file"""


def read_file(filename=""):
    """module reads a file and prints it to stout"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
