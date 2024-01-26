#!/usr/bin/python3
# 4-square.py
""" Defines class Square """


class Square:
    """ Build awesome square"""

    def __init__(self, size=0):
        """intialize a square

            Args:
                size(int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """ retrives size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of square based on conditions

            Args:
                value: value passed by user

            Raises:
                TypeError: size must be an integer
                ValueError: value must be not less than 0
        """
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ calculates the area of the square

            Return:
                    area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the charchter # """
        j = 0
        i = 0

        if self.__size == 0:

            print("")
        else:
            for i in range(self.size):
                for i in range(self.size):
                    print('#', end="")
                print()
