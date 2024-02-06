#!/usr/bin/python3
import json
""" attribute defined to_json_string"""


def to_json_string(my_obj):
    """ function to return JSON string from python object"""
    return json.dumps(my_obj)
