#!/usr/bin/python3

def no_c(my_string):

    char_rem = "Cc"
    modified_str = ""

    for char in my_string:
        if char not in char_rem:
            modified_str += char

    return (modified_str)
