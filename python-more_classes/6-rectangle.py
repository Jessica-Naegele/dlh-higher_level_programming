#!/usr/bin/python3
"""Modules creates a class to calculate rectangle's area and perimeter"""


class Rectangle:
    """Rectangle caclulates area, perimeter and able to delete"""

    # class attribute
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialisation of default values 0 for width and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    # __str__
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return "\n"
        else:
            list = []
            for i in range (self.__height):
                list.append("#" * self.__width)
            return "\n".join(list)

    # __eval__
    def __eval__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    # delete rectangle
    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle ...")
