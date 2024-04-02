#!/usr/bin/python3
""" A python module that Posts an email to a url using
    request module
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    mail_value = {'email': sys.argv[2]}

    response = requests.post(url, data=mail_value)
    print(response.text)
