#!/usr/bin/python3
""" module defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """ insersts text after each line containing a given string in a file
    """
    t = ""
    with open(filename) as f:
        for line in f:
            t += line
            if search_string in line:
                t += new_string
    with open(filename, "w") as w:
        w.write(t)
