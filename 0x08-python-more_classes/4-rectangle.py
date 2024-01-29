#!/usr/bin/python3
# 2-rectangle.py
""" Calss Determines Rectangle """


class Rectangle:
    """ defines awesome rectangle by implementing"""

    @property
    def width(self):
        """ retrives width for rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set values of width based on the condition

            Args:
                Value: value to be passed by user

            Raises:
                TypeError: width must be an integer
                ValueError: width must be >= 0
        """

        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """ retrives value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ set a value of height based on conditions

            Args:
                value: value to be passed by user

            Raises:
                TypeError: height must be an integer
                ValueError: value must be not less than zero
        """

        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

    def __init__(self, width=0, height=0):
        """ passes intial value to object

            Args:
                width: width of rectangle
                height: height of rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """ returns area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """ returns the rectangle perimeter"""

        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self) -> str:
        """ build diagram for rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for col in range(self.__height):
            for row in range(self.__width):
                rect += "#"
            if col < self.height - 1:
                rect += "\n"
        return (rect)

    def __repr__(self) -> repr:
        """ return a string representation of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
