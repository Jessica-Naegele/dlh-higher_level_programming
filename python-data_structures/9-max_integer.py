#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        j = -300000000000
        for i in range(len(my_list)):
            if my_list[i] > j:
                j = my_list[i]
        return j
