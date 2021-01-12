#!/usr/bin/python3
"""sends request to URL and displays response"""
from sys import argv
from urllib import request
from urllib import error

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as f:
            print(f.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
