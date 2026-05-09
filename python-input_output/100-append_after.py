#!/usr/bin/python3
"""Module inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string after each line containing search_string"""
    res_line = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            res_line.append(line)
            if search_string in line:
                res_line.append(new_string)
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(res_line)
