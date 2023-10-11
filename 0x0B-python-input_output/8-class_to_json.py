#!/usr/bin/python3
"""a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary of simple data structure."""
    return obj.__dict__
