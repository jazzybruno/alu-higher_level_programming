#!/usr/bin/python3
"""Defines matrix_divided, which divides every element of a matrix."""


def matrix_divided(matrix, div):
    """Return a new matrix with each element divided by div, rounded to 2.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats, if rows
            have different sizes, or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(n, (int, float)) and not isinstance(n, bool)
                    for row in matrix for n in row)):
        raise TypeError(msg)
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
