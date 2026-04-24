#!/usr/bin/python3
import sys 

if __name__ == "__main__":
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:") 
        print(sys.argv[1])
    else:
        print("{} agruments:".format(count))
        for i in range(1, count+1):
            print(sys.argv[i])
