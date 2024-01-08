#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence != '':
        f_char = sentence[0]
    else:
        f_char = None
    return(len(sentence), f_char)
