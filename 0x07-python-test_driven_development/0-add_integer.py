#!/usr/bin/python3
"""

add_intger: adds two integers

"""


def add_integer(a, b=98):
    """add two integers
        Args:
            a: first number
            b: second number
        Raises:
            TypeError: a or b must be integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
