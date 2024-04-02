#!/usr/bin/python3
"""A script tha:
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_use/
"""
import sys
import requests


if __name__ == "__main__":
    my_letter = "" if len(sys.argv) == 1 else sys.argv[1]
    my_payload = {"q": my_letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=my_payload)
    try:
        url_response = r.json()
        if url_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(url_response.get("id"), url_response.get("name")))
    except ValueError:
        print("Not a valid JSON")
