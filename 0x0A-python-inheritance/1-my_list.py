#!/usr/bin/python3
""" list inheritance """


class MyList(list):
    def print_sorted(self):
        """ Prints a list in ascending order """
        print(sorted(self))
