#!/usr/bin/python3

def multiple_returns(sentence):
    first_char = ()
    if sentence != '':
        first_char = len(sentence), sentence[0]
    else:
        first_char = 0, "None"
    return first_char
