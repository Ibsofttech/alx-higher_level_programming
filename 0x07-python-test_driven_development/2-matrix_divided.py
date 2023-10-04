#!/usr/bin/python3
""" Defines a functuon matrix_divided
    Errors:
            TypeError: if matrix is not a list of lists
            TypeError: if the matrix is not of the same size
            ZeroDivisionError: if the divisor of the matrix is 0
"""


def matrix_divided(matrix, div):
    """ The function the divides a matrix
        Arguments:
            matrix: a list of lists containing floats or integers
        div:
            the divisor
        Return:
            a new matrix whose value has been divided
    """
    new_matrix = []
    if (not isinstance(div, float) and not isinstance(div, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")
    try:
        size = len(matrix[0])
    except Exception:
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix"
                            "(list of lists) of integers/floats")
        if len(i) != size:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for number in i:
            if not isinstance(number, int) and not isinstance(number, float):
                raise TypeError("matrix must be a matrix"
                                "(list of lists) of integers/floats")
            init = float(number / div)
            ans = float("{:.2f}".format(init))
            new_row.append(ans)
        new_matrix.append(new_row)
    return new_matrix
