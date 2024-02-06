#!/usr/bin/python3
""" module define python class-to-JSON function"""


def class_to_json(obj):
    """Returns dictionaty representation of a simple data structure"""
    return obj.__dict__
