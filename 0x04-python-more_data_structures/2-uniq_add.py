#!/usr/bin/python3

def uniq_add(my_list=[]):
    sumadd = 0
    for i in set(my_list):
        sumadd += i
    return sumadd
