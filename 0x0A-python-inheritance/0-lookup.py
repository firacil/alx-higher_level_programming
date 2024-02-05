#!/usr/bin/python3
''' defineing dunction lookup that returns of available attr'''


def lookup(obj):
    ''' function to list availabile attributes and methods of object

    Args:
        obj: object to inspect
    Return:
        list of attributes and methods.
    '''
    return dir(obj)
