#!/usr/bin/python3
"""This module is about defining a class Square"""


class Square:
    """This is a class square defined by size and calculates the area"""
    def __init__(self, size=0):
        """Initiatlize"""
        self.__size = size
        if isinstance(size, int) is not True:
            raise ValueError("size must be >= 0")
        if size < 0:
            raise TypeError("size must be an integer")

    def area(self):
        area = self.__size ** 2
        return area
