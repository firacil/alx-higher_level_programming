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
        """ retreves a dictionary representation of a Student"""
        return self.__dict__
