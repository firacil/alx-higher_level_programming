#!/usr/bin/python3
"""module will create function pascal_triangle"""


def pascal_triangle(n):
    """ returns a list of lists of integer representating
        pascal triangle of n
    """
    triangle = []
    if n <= 0:
        return []

    for i in range(n):
        row = [1] * (i + 1) # intialize each row
        if i >= 2:
            for j in range(1, i): # skip the first and last element of the row
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
