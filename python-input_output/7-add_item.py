#!/usr/bin/python3
"""Add Item with 5 & 6"""

# import sys and save_to_json_file and load_from_json_file
import sys 
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import os

if __name__ == "__main__":
    # test whether file exists
    if os.path.exists("add_item.json") == False:
        # create a new file:
        with open("add_item.json", "w", encoding="utf-8") as f:
            f.write("[]")  
    # append to file
    content = load_from_json_file("add_item.json")  # store existing content
    count = len(sys.argv) - 1
    my_list = sys.argv[1:]
    content.extend(my_list)
    save_to_json_file(content, "add_item.json")
