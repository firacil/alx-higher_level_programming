#!/usr/bin/python3
''' define function that do instances'''


def inherits_from(obj, a_class):
    ''' function that returns 'True'
        if the object is an instance of class that
        inherted(directly of indirectly) from the
        specified class
    '''
    return isinstance(obj, a_class) and issubclass(type(obj), a_class)
