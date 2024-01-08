#!/usr/bin/python3

def multiple_returns(sentence):

    if sentence == '':
        fchar = None
    else:
        fchar = sentence[0]
    return(len(sentence), fchar)
