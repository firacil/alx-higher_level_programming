#!/usr/bin/python3
""" function divide all elements of matrix"""


def matrix_divided(matrix, div):
    """ function to divide mtrix

        Args:
            matrix: matrix to be divided
            div: number to be pass

        Raises:
            TypeError: when type error occured
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists.")

    if not all(isinstance(element, (int, float))for row in matrix for element in row):
        raise TypeError("Matrix must be a mtrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0])
       for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2)
                for element in row] for row in matrix]

    return new_matrix
