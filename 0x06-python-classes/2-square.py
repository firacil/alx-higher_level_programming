#!/usr/bin/python3
# 0-square.py
""" Define a class Square """


class Square():
    """ Describe a Square"""

    def __init__(self, size=0):
        """Initialize a new Square


        Args:
            size(int): the size of the square


        Raises:
            TypeError: when size failed to be number
            ValueError: size must be >= 0


        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be a number")

        if size < 0:
            raise ValueError("size must be >= 0")
