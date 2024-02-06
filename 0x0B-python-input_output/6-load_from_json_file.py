#!/usr/bin/python3
""" module thats create object from a JSON file"""
import json


def load_from_json_file(filename):
    """function creates an object from a "JSON file"""
    with open(filename, 'r') as File:
        return json.load(File)
