#!/usr/bin/python3
def safe_print_integer(value):
    a = False
    try:
        print("{:d}".format(value))
        a = True
    except (ValueError, TypeError):
        pass
    finally:
        return a
