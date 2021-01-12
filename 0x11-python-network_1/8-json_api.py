#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        d = r.json()
        if d:
            print("[{}] {}".format(d.get('id'), d.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
