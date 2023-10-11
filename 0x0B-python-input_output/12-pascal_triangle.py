#!/usr/bin/python3
"""a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triang = [[1]]
    while len(triang) != n:
        tri = triang[-1]
        tmp = [1]
        for idx in range(len(tri) - 1):
            tmp.append(tri[idx] + tri[idx + 1])
        tmp.append(1)
        triang.append(tmp)
    return triang
