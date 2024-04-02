#!/usr/bin/python3
""" A module that fetches
    alx-intranet.hbtn.io status
    Using requeats package
"""
import requests


url = 'https://alx-intranet.hbtn.io/status'
a_request = requests.get(url)
print("Body response:")
print(f"\t- type: {type(a_request.text)}")
print(f"\t- content: {a_request.text}")
