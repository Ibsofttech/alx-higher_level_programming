#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    url_response = requests.get(url)
    if url_response.status_code >= 400:
        print(f"Error code: {url_response.status_code}")
    else:
        print(url_response.text)
