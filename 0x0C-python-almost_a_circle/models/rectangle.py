#!/usr/bin/python3
"""Define class Rectangle that inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """ class that defines and implements rectangle"""

    @property
    def width(self):
        """retrives width ("getter")"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set value according to its value"""
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """retrives width ("getter")"""
        return self.__width

    @height.setter
    def height(self, value):
        """ set value according to its value"""
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """retrives data x"""
        return self.__x

    @x.setter
    def x(self, value):
        """value setter"""
        if isinstance(value, int):
            self.__x = value
        else:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """retrives data y"""
        return self.__y

    @y.setter
    def y(self, value):
        """value setter"""
        if isinstance(value, int):
            self.__y = value
        else:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

    def __init__(self, width, height, x=0, y=0, id=None):
        """Contructor for rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)  # calling super class Base..
