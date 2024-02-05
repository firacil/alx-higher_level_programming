#!/usr/bin/python3
''' function define object passed is instance or not
    of specifed class
'''


def is_same_class(obj, a_class):
    ''' function check for specified instance

        Returns:
            True: if object is instance
            False: if not
    '''
    return isinstance(obj, a_class) and type(obj) is a_class
