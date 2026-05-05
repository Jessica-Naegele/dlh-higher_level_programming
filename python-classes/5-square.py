#!/usr/bin/python3
"""This module is about creating a class Square"""


class Square:
    """This class square is defined by size delivering the area and my_print"""

    def __init__(self, size=0):
        """Initializing - if no size is delivered default 0 will be used"""
        self.__size = size

    @property
    def size(self):
        """getter property size"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter property is size"""
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        area = __size ** 2
        return area

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
