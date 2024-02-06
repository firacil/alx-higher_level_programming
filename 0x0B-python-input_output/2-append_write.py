#!/usr/bin/python3
""" defined function append_write"""


def append_write(filename="", text=""):
    """ function that append string at the end"""
    with open(filename, 'a', encoding="utf") as myFile:
        return(myFile.write(text))
