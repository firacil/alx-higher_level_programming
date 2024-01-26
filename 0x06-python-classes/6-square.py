#!/usr/bin/python3
# 5-square.py
""" Defines class square"""

class Square:
    """ Build awesome square feature"""

    def __init__(self, size=0, position=(0, 0)):
        """ Intialization of square

            Args:
                size(int): size of the square
                position: position of two tuple

        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ retrives size for square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ set value to size based on condition

            Args:
                value: value passed by user

            Raises:
                TypeError: size must be integer
                ValueError: value must be not less than 0

        """
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """ retrive position of square """
        return self.__position

    @position.setter
    def position(self, value):
        """ set position based on the condition
