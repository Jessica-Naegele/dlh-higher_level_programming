#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        new_list = [(x * y) for x, y in my_list]
        j = []
        for i in range(0, len(my_list)):
            j.append(my_list[i][1])
        return sum(new_list)/sum(j)
