#!/usr/bin/python3
"""Defining Class Base"""
import os
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None:
            return "[]"
        else:
            j_string = json.dumps(list_dictionaries)
            return j_string

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, 'w') as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of JSON string representation json_string"""

        json_list = []

        if json_string is not None and json_string != '':
            json_list = json.loads(json_string)

        return json_list
