#!/usr/bin/python3
"""function to read a file"""


def read_file(filename=""):
    """ function that read passed file"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
