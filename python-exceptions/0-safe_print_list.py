#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        # We hit the end of the list before reaching x
        pass
    finally:
        # This runs whether we hit an error or not
        print("")
    return count
