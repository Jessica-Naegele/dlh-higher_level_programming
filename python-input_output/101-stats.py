#!/usr/bin/python3
"""Log Parser"""

import sys

status = {
    "200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
    "405": 0, "500": 0
}
total_size = 0
line_count = 0

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            parts = line.split()

            if len(parts) < 2:
                continue

            status_code = parts[-2]
            file_size = int(parts[-1])

            total_size += file_size
            if status_code in status:
                status[status_code] += 1
            line_count += 1

            # Print every 10 lines
            if line_count % 10 == 0:
                print("File size: {}".format(total_size))
                for code in sorted(status.keys()):
                    if status[code] > 0:
                        print("{}: {}".format(code, status[code]))

    except KeyboardInterrupt:
        # Handles manual interruption (Ctrl+C)
        print("File size: {}".format(total_size))
        for code in sorted(status.keys()):
            if status[code] > 0:
                print("{}: {}".format(code, status[code]))
        raise

    # --- THIS FIXED IT ---
    # This runs when sys.stdin closes normally (e.g., cat file_0 finishes)
    print("File size: {}".format(total_size))
    for code in sorted(status.keys()):
        if status[code] > 0:
            print("{}: {}".format(code, status[code]))
