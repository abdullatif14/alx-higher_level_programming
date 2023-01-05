#!/usr/bin/python3

""" A function that divides all elements of a function"""


def matrix_divided(matrix, div):
    """ a function that divides a matrix is a matrix"""

    if not all(isintance(row, list) for row in matrix):
        error('matrix must be a matrix (list of lists) of integers/floats')
        raise TypeError(error)
    if not all(type(element, (int, float)) for row in matrix for item in row):
        error1('matrix must be a matrix (list of lists) of integers/floats')
        raise TypeError(error1)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if not isintance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(element / div, 2) for element in row] for row in matrix]
