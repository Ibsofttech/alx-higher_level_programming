#!/usr/bin/python3
"""
    A funtion that adds two integers

    Raise a TypeError if a or b is not an integer
"""


def add_integer(a, b=98):
    """
        Returns the additional sum of the two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b