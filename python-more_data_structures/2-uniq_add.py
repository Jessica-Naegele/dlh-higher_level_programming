#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        add_list = my_list
    else:
        add_list = [my_list[0]]
        for i in my_list:
            if i not in add_list:
                add_list.append(i)
    r = sum(add_list)
    return r
