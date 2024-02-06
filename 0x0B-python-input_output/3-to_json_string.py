#!/usr/bin/python3
""" attribute defined to_json_string"""
import json


def to_json_string(my_obj):
    """ function to return JSON string from python object"""
    return json.dumps(my_obj)
