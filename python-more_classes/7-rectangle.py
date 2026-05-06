#!/usr/bin/python3
"""This module defines the class Rectangle"""


class Rectangle:
    """This class calculates the area and perimeter of a rectangle"""

    # public class attributes
    number_of_instances = 0
    print_symbol = []

    def __init__(self, width=0, height=0, print_symbol="#"):
        """Initialisation of default values 0 for width and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
        self.print_symbol = print_symbol

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

    # print stored in print_symbol
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return "\n"
        else:
            list = []
            for i in range(self.__height):
                list.append(str(self.print_symbol) * self.__width)
        return "\n".join(list)

    # deletion
    def __del__(self):
        type(self).number_of_instances -= 1
        print("By rectangle...")
