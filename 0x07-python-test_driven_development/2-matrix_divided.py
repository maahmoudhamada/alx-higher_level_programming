#!/usr/bin/python3

"""The matrix_divided module

Functions:
    matrix_divided
"""


def matrix_divided(matrix, div):
    """Return a list of lists contains results of matrix/div
    Args:
        matrix: List of lists contains integers/floats elements
        div: Integer/float to divide with it
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
        of integers/floats")
    if not all(isinstance(row, list) for row in matrix) or not \
            all(isinstance(el, (int, float)) for r in matrix for el in r):
        raise TypeError("matrix must be a matrix \
            (list of lists) of integers/floats")
    elif not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return [[round(elem / div, 2) for elem in row]for row in matrix]
