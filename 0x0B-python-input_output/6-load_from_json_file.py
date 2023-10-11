#!/usr/bin/python3
"""module defination"""
import json


def load_from_json_file(filename):
    """return Created Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
