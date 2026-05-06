#!/usr/bin/python3
"""Module creates class Rectangle"""


class Rectangle:
    """Class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

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
            raise TypeError("width must be an integer")
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

    # deletion of instance
    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    # STR print_symbol
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return "\n"
        else:
            list = []
            for i in range(self.__width):
                list.append(self.print_symbol * self.__width)
            return "\n".join(list)

    # eval
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    # static method bigger
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() == rect_2.area():
                return rect_1
            elif rect_1.area() > rect_2.area():
                return rect_1
            else:
                return rect_2

    # Class method square
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
