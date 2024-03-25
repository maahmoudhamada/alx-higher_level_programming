#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if matrix == [[]]:
        print()
        return
    else:
        for x in matrix:
            ln = len(x)
            for y in range(ln):
                print("{:d}".format(x[y]), end='\n' if y == ln - 1 else ' ')
