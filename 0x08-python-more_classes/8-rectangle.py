#!/usr/bin/python3
# 2-rectangle.py
""" Calss Determines Rectangle """


class Rectangle:
    """ defines awesome rectangle by implementing"""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
                try:
                    rect += str(self.print_symbol)
                except Exception:
                    rect += type(self).print_symbol
            if col < self.height - 1:
                rect += "\n"
        return (rect)

    def __repr__(self) -> repr:
        """ return a string representation of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle

            Args:
                rect_1: rectangle one to be checked
                rect_2: rectangle two to be checked

            Raises:
                TypeError: rect_1 must be instance of Rectangle and rect_2 same
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
