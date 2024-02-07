#!/usr/bin/python3
"""Module inherits from the list class"""


class MyList(list):
    """class MyList inherits parent class list"""
    def print_sorted(self):
        """function that prints sorted list"""
        print(sorted(self))
