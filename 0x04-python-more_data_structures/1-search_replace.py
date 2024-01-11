#!/usr/bin/python3
def search_replace(my_list, search, replace):
    search = 2
    replace = 89

    new_list = [replace if x == search else x for x in my_list]

    return (new_list)
