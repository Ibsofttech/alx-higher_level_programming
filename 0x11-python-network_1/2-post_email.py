#!/usr/bin/python3
""" python module that sends a POST requeat to a url of an
    email passed as parameters and displays the body
    of the response (decoded in utf-8)....
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    my_data = urllib.parse.urlencode(value)
    my_data = my_data.encode('ascii')  # or utf-8
    _request = urllib.request.Request(url, my_data)
    with urllib.request.urlopen(_request) as response:
        print(response.read().decode('utf-8'))
