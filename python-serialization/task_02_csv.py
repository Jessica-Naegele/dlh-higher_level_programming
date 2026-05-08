#!/usr/bin/env python3
"""function converts CVS into json"""

import json
import csv


def convert_csv_to_json(filename):
    """function converts data from cvs into data.json"""
    try:
        content = []
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                content.append(row)
        print(reader)
        print(content)
        with open("data.json", "w") as jsfile:
            jsfile.write("[")
            for row in content:
                jsfile.write("\n")
                json.dump(row, jsfile)
            jsfile.write("\n]")
        return True
    except (FileNotFoundError, EOFError):
        return False
