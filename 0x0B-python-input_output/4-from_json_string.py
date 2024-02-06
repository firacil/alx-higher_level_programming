#!/usr/bin/python3
""" module that return python object from Json string"""
import json


def from_json_string(my_str):
    """ attribute to return py object"""
    return json.loads(my_str)
