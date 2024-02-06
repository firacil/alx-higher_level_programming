#!/usr/bin/python3
""" Class BaseGeometry"""


class BaseGeometry:
    """ class Basegeometry"""

    def area(self):
        """ raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function that validates value

            Args:
                name: is always string
                value: integer

            Raises:
                TypeError: if value is not integer
                ValueError: if value is less than or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
