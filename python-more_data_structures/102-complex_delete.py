#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = dict()
    t = False
    for i in a_dictionary:
        if a_dictionary[i] == value:
            t = True
    if t:
        for j in a_dictionary:
            if a_dictionary[j] == value:
                new_dict[j] = a_dictionary[j]
        a_dictionary = new_dict
    return a_dictionary
