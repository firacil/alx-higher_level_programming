#!/usr/bin/python3
"""Defining Class Base"""
import os
import turtle
import json
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """returns an instances with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = cls.__name__ + ".json"
        list_of_inst = []
        list_dic = []

        if os.path.exists(filename):
            with open(filename, 'r') as file_list:
                my_str = file_list.read()
                list_dic = cls.from_json_string(my_str)
                for d in list_dic:
                    list_of_inst.append(cls.create(**d))
        return list_of_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes list_objs and saves to file"""

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as filecsv:
            if list_objs is None or list_objs == []:
                filecsv.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                wr = csv.DictWriter(filecsv, fieldnames=fieldnames)
                for obj in list_objs:
                    wr.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file"""

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dic = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dic = [dict([k, int(v)]
                            for k, v in d.items()) for d in list_dic
                            ]
                return [cls.create(**d) for d in list_dic]
        except IOError:
            return []

    @staticmethod
    def draw (list_rectangles, list_squares):
        '''
            Draw rectangles and squares using turtle mod
            Args:
                list_rectangles
                list_squares
        '''
        t = turtle.Turtle()
        t.screen.bgcolor("#b7312c")
        t.pensize(3)
        t.shape("turtle")

        t.color("#ffffff")
        for r in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(r.x, r.y)
            t.down()
            for i in range(2):
                t.forward(r.width)
                t.left(90)
                t.forward(r.height)
                t.left(90)
            t.hideturtle()

        t.color("#b5e3d8")
        for s in list_squares:
            t.showturtle()
            t.up()
            t.goto(s.x, s.y)
            t.down()
            for i in range(2):
                t.forward(s.width)
                t.left(90)
                t.forward(s.height)
                t.left(90)
            t.hideturtle()

        t.exitonclick()
