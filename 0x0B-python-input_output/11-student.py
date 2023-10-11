#!/usr/bin/python3
"""define a a class Student """


class Student:
    """ Defines a new student with some attributes """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns only attrs in attrs, else the dict of the class """
        if type(attrs) == list and all(type(idx) == str for idx in attrs):
            return {k: getattr(self, k) for k in attrs if k in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
