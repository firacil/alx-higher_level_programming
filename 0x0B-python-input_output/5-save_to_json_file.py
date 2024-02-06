#!/usr/bin/python3
""" module to writes object to textfile"""
import json


def save_to_json_file(my_obj, filename):
    """attribute to writes and object to text file
        using a JSON representation
    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        return json.dump(my_obj, myFile)
