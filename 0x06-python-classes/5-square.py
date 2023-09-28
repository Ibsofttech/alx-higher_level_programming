#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Square representation"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Returns the new size of tne Square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setting the size of Square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with #"""
        for symb in range(0, self.__size):
            [print("#", end="") for symb2 in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
