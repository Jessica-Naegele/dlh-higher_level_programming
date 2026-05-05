#!/usr/bin/python3
"""This module defines class Square"""


class Square:
    """This class Square is defined by size"""
    def __init__(self, size=0):
        """Initialize square if no size is given, it is defaulting to 0"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """This is a setter"""
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        area = self.__size ** 2
        return area
