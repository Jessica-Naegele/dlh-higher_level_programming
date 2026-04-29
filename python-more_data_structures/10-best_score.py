#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    elif a_dictionary is {}:
        return None
    else:
        return max(a_dictionary, key=a_dictionary.get)
