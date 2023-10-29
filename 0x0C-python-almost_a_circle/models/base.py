#!/usr/bin/python3
import json


class Base:
    """ The Bases of all other classes to be created """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor: Initializes the 'id' field"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method: Converts a list of dictionaries to a JSON string"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method: Writes a JSON string to a file"""
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as file:
            serialized_data = []
            if list_objs:
                serialized_data = [obj.to_dictionary() for obj in list_objs]
            file.write(Base.to_json_string(serialized_data))

    @staticmethod
    def from_json_string(json_string):
        """Static method: Converts a JSON string to a list of dictionaries"""
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with attributes set from a dictionary"""
        if cls.__name__ == 'Square':
            my_dum = cls(5)
        else:
            my_dum = cls(2, 4)
        my_dum.update(**dictionary)
        return my_dum
