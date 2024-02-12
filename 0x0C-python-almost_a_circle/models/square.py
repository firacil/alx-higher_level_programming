#!/usr/bin/python3
"""Defines class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class implements square of rec"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor method for Square class"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ overload __str__ methon"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """ getter of size"""
        return self.__width

    @size.setter
    def size(self, value):
        """ setter of size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """public method that assign attribute"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of rectangle"""
        o_dic = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

        return (o_dic)
