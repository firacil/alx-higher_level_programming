#!/usr/bin/python3
def print_list_integer(my_list=[]):

    if len(my_list) != 0:
        for i in range(len(my_list)):
            print('{:d}'.format(my_list[i]))
