#!/usr/bin/python3
""" A python module that sends a request tona url and displays
    the header with variable X-Request-od
"""
import requests
import sys


if __name__ == "__main__":
    my_req = requests.get(sys.argv[1]).headers
    print(my_req.get("X-Request-Id"))
