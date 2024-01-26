#!/usr/bin/python3
# 3-square.py

class Square:
    """Defines a square based on 3-square.py"""

    def __init__(self, size=0):
        """ Initialize the class

        Args:
            size(int): size of the square

        """
        self.size = size

    @property
    def size(self):
        """ this is getter for size of the square
            it retrives size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for the size of square

            Args:
                value: value passed by the user
            Raises:
                TypeError: size must be integer
                ValueError: size must be not less than 0

            it checks wheteher value have to be passed or not
            using conditions
        """

        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ function to calculate the area of square

            Return:
                    area of the square
        """

        return self.__size ** 2
