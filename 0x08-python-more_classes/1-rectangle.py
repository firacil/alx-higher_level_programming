#!/usr/bin/python3
# 0-ractangle.py
""" Class Determines rectangle """


class Rectangle:
    """ Build awesome implementation of rectangle """

    def __init__(self, width=0, height=0):
        """ Intalize class

            Args:
                width: width of height
                height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrives width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set value width based on condtions

            Args:
                value: value that will passed from user

            Raises:
                TypeError: width must be an integer
                ValueError: value must be >= 0
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
        """ sets height value based on the conditions

            Args:
                value: value to be passed as height be user
            Raises:
                TypeError: height must be an intger
                ValueError: Value must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
