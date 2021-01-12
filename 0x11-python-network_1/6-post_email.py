#!/usr/bin/python3
"""sends POST reqsuest to passed URL with email as parameter"""
from sys import argv
import requests

if __name__ == "__main__":
    p = {'email': argv[2]}
    r = requests.post(argv[1], data=p)
    print(r.text)
