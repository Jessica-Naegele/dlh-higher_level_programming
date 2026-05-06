#!/usr/bin/python3
"""This module is creating the class Rectangle"""


class Rectangle:
    """This class is clculating the area and perimeter of a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("message height must be >= 0")
        else:
            self.__height = height

    def area(self):
        area = self.__height * self.__width
        return area

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        rec = []
        for i in range(self.__height):
            rec.append("#" * self.__width)
        return '\n'.join(rec)
