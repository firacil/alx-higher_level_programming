#!/usr/bin/python3
''' Class MyList defined'''


class MyList(list):
    ''' class MyList inherits parent class 'list"'''

    def print_sorted(self):
        ''' function that prints sorted list'''
        sorted_list = sorted(list(self))
        print(sorted_list)
