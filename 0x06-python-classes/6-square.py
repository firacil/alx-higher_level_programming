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

            Args:
                value: value passed from user

            Raise:
                TypeError: postion must be a tuple of 2 positive integers

         """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ returns the area of the square

        Return:
            area of square
        """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the charachter # """

        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.size):
            for _ in range(self.__position[0]):
                print(' ', end="")

            for _ in range(self.__size):
                print("#", end="")
            print()
