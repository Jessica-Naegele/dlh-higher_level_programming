#!/usr/bin/python3
"""Log Parser"""

import sys
# for line in sys.stdin:  # checks what is currently the input from stdin

# dictionary to save everything? Dict = {(status_count) : code}
status = {
    "200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
    "405": 0, "500": 0}
# total file size
total_size = 0
line_count = 0

""" Input format: <IP Address> - [<date>]
"GET /projects/260 HTTP/1.1" <status code> <file size>"""
if __name__ == "__main__":
    try:
        for line in sys.stdin:
            parts = line.split()

            # skipping lines that don't have enough data
            if len(parts) < 2:
                continue

            # creates a list with every single aspect of the input
            status_code = parts[-2]  # 2. letztes Attribut in der Liste
            file_size = int(parts[-1])  # letztes Attribut in der liste
            # add values to total_size and status
            total_size += file_size
            if status_code in status:
                status[status_code] += 1
            line_count += 1
            # to enable printing after every 10th line
            if line_count % 10 == 0:
                # print must be inside the loop, otherwise, it will not print
                print("File size: {}".format(total_size))
                for code in sorted(status.keys()):
                    if status[code] > 0:
                        print("{}: {}".format(code, status[code]))
    except KeyboardInterrupt:
        print("File size: {}".format(total_size))
        for code in sorted(status.keys()):
            if status[code] > 0:
                print("{}: {}".format(code, status[code]))
