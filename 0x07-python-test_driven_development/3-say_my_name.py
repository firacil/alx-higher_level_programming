#!/usr/bin/python3
""" defines function that print names"""


def say_my_name(first_name, last_name=""):
    """ prints names based on condition

        Args:
            first_name: first name to be passed
            last_name: last name to be passed

        Raises:
            TypeError: when type error occured
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
