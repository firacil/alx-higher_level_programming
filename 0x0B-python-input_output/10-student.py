#!/usr/bin/python3
""" module that define class Student"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """ instantiation of class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retreves a dictionary representation of a Student
            if attrs is alist of strings, represents only attributes specifed
            otherwise all of them
        """
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, k)}
        return self.__dict__
