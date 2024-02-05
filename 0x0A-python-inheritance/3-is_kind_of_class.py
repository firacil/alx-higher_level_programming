#!/usr/bin/python3
''' function to check instance form inherted class'''


def is_kind_of_class(obj, a_class):
    ''' function checks for instance between child and parent class

        Returns:
            True: if object is an instance of class that inherited from.
    '''
    return isinstance(obj, a_class)
