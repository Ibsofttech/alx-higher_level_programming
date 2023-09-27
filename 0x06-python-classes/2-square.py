#!/usr/bin/python3
"""A class with name Square"""


class Square:
    def __init__(self, size=0):
        """Attribute and methods defination"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
