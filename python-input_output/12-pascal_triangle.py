#!/usr/bin/python3
"""
    This module creates a lists of integers
    representing the Pascal's triangle
"""


def pascal_triangle(n):
    """
        This function creates a list of integers
        representing the Pascal's triangle
    """
    l1 = []

    for i in range(0, n):  # rows
        l2 = [1]
        if i >= 1:
            for j in range(1, i):  # line item
                x = l1[i-1][j-1] + l1[i-1][j]
                l2.append(x)
            # add last value to l3
            l2.append(1)
        # update l2
        l1.append(l2)
    return l1
