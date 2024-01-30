#!/usr/bin/python3
""" function prints a square"""


def print_square(size):
    """ print square based on size using #

        Args:
            size: size length of the square

        Raises:
            TypeError: when type error occured
            ValueError: when value is not printed as expected
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for i in range(size):
            print("#", end="")
        print()
