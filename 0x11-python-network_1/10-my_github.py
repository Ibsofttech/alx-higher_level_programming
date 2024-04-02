#!/usr/bin/python3
"""A script that:
- takes your GitHub credentials (username and password)
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    authen = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=authen)
    print(r.json().get("id"))
    