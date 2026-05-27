#!/usr/bin/python3
"""This is a module for creating class Square"""


class Square:
    """This class is calculating the area of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing for missing size and position default 0"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter Size"""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area calculated of a square"""
        area = self.__size ** 2
        return area

    def __eq__(self, other):
        """equal to"""
        return self.area() == other.area()

    def __ne__(self, other):
        """not equal to"""
        return self.area() != other.area()

    def __lt__(self, other):
        """ lower to"""
        return self.area() < other.area()

    def __le__(self, other):
        """lower and equal to"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """greater to"""
        return self.area() > other.area()

    def __ge__(self, other):
        """greater and equal to"""
        return self.area() >= other.area()
