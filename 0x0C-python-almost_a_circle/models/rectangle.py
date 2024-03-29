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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if type(value) == bool:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrives width ("getter")"""
        return self.__height

    @height.setter
    def height(self, value):
        """ set value according to its value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if type(value) == bool:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrives data x"""
        return self.__x

    @x.setter
    def x(self, value):
        """value setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if type(value) == bool:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrives data y"""
        return self.__y

    @y.setter
    def y(self, value):
        """value setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if type(value) == bool:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """Contructor for rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)  # calling super class Base..

    def area(self):
        """ return area of rectangle"""
        width = self.__width
        height = self.__height

        return (width * height)

    def display(self):
        """ prints in stdout the Rectangle
            instance with the character '#'
        """
        for _ in range(self.__y):
            print()  # print y blank lines for y coord

        #  print each row of the rec
        for i in range(self.__height):
            #  print x spaces for x coord
            print(" " * self.__x, end="")
            #  print '#' for width
            print("#" * self.__width)

    def __str__(self):
        """returns Rectangle values"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
                    self.id, self.__x,
                    self.__y, self.__width, self.__height

                    ))

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute"""
        if args:  # if *args working
            attr = ['id', 'width', 'height', 'x', 'y']
            for att, value in zip(attr, args):
                setattr(self, att, value)
        elif kwargs:  # if **kwargs working
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns dictionary representation of Rectangle"""
        o_dic = {'id': self.id, 'width': self.__width,
                 'height': self.__height,
                 'x': self.__x, 'y': self.__y
                 }

        return o_dic
