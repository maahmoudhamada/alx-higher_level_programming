#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Return a square matrix copy """
    mtx = [[y*y for y in x]for x in matrix]
    return mtx
