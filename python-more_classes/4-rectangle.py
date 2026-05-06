#!/usr/bin/python3
"""Creation of class rectangle"""


class Rectangle:
    """Calculation of area, perimeter, with repr and eval"""

    def __init__(self, width=0, height=0):
        """Initialisation with default 0 for height and width"""
        self.width = width
        self.height = height

# private instance width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

# private instance height
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

# public instance methode area
    def area(self):
        area = self.__height * self.__width
        return area

# publich instance method perimeter
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width * self.__height)
        return perimeter

# STR
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return "\n"
        else:
            list = []
            for i in range(self.__height):
                list.append("#" * self.__width)
        return '\n'.join(list)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
