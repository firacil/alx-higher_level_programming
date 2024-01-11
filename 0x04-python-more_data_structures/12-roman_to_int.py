#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    tot_al = 0
    digs = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for rom in reversed(roman_string):
        a = digs[rom]
        tot_al += a if tot_al < a * 5 else -a
    return tot_al
