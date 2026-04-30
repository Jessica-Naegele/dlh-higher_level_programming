#!/usr/bin/python3
def safe_print_division(a, b):
    r = None
    try:
        r = a / b
    except ZeroDivisionError:
        pass
    except TypeError:
        pass
    except ValueError:
        pass
    finally:
        print("Inside result: {}".format(r))
        return r
