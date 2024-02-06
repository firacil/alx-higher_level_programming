#!/usr/bin/python3
""" define function write_file"""


def write_file(filename="", text=""):
    """function writes a string to text file
    and returns the number of charchter written
    """
    with open(filename, 'w+', encoding="utf-8") as myFile:
        count = myFile.write(text)
        return count
