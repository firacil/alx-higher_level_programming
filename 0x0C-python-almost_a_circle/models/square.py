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
