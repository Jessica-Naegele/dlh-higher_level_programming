#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        new_list = []
        for i in range(0, list_length):
            try:
                d = my_list_1[i] / my_list_2[i]
                new_list.append(d)
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
                pass
            except TypeError:
                print("wrong type")
                new_list.append(0)
                pass
            except IndexError:
                print("out of range")
                new_list.append(0)
                pass
    finally:
        return new_list
