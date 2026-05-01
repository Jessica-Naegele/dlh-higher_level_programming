#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    d = False
    try:
        print("{:d}".format(value))
        d = True
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err))
    finally:
        return d
