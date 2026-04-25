#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = len(sys.argv)
    int_agrv = [int(arg) for arg in sys.argv[1:]]
    sum = 0
    if count == 0:
        print(sum)
    else:
        for i in range(0, count-1):
            sum = sum + int_agrv[i]
        print(sum)
