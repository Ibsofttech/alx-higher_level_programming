#!/usr/bin/python3
"""define a class Student """


class Student:
    """ Defines a new student with some attributes """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns the dictionary of the class """
        return self.__dict__
