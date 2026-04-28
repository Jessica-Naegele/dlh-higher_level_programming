#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b_dic = sorted(a_dictionary)
    for i in b_dic:
        print("{}: {}".format(i, a_dictionary.get(i)))
