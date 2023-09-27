#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value:
        return a_dictionary
    else:
        return {key: val for key, val in a_dictionary.items() if val != value}
