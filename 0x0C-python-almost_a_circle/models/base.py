#!/usr/bin/python3
"""Defining Class Base"""


class Base:
    """Defined class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
