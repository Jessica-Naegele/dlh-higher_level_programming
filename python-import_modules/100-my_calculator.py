#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
if __name__ == "__main__":
    count = len(argv)
    if count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] == "+":
        a = int(argv[1])
        b = int(argv[3])
        c = add(a,b)
        print("{} + {} = {}".format(a, b, c))
    elif argv[2] == "-":
        a = int(argv[1])
        b = int(argv[3])
        c = sub(a,b)
        print("{} - {} = {}".format(a, b, c))
    elif argv[2] == "*":
        a = int(argv[1])
        b = int(argv[3])
        c = mul(a,b)
        print("{} * {} = {}".format(a, b, c))
    elif argv[2] == "/":
        a = int(argv[1])
        b = int(argv[3])
        c = div(a,b)
        print("{} / {} = {}".format(a, b, c))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
