#!/usr/bin/python3
# 0-square.py
""" Define a class Square """


class Square():
    """Describe a Square"""

    def __init__(self, size=0):
        """Initialize a new Square

        Args:
            size(int): The size of square

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0

        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Calculate current square area

        Arg:

        Return:
            current square area

        """
        return self._size**2
