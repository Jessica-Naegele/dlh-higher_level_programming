#!/usr/bin/python3
"""This module creates the class Rectangle"""


class Rectangle:
    """Class Rectangle calculates the area perimeter"""

    def __init__(self, width=0, height=0):
        """Initialisation of default values 0 for width and height"""
        self.width = width
        self.height = height

    # private instance width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("widht must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    # private instance attribute height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    # pubich instance methode def area
    def area(self):
        area = self.__height * self.__width
        return area

    # public instance method perimeter
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__height + self.__width)
        return perimeter

    # return a # Rectangle
    def __str__(self):
        if self.__height == 0 or self.__width:
            return '\n'
        else:
            list = []
            for i in range(self.__height):
                list.append("#" * self.__width)
            return "\n".join(list)

    # repr representation of rectangle
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    # print del Rectangle
    def __del__(self):
        print("Bye rectangle...")
