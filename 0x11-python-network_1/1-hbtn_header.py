#!/usr/bin/python3
"""Takes URL and displays value of X-Request-Id in header response"""
from sys import argv
from urllib import request

if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as f:
        print(f.headers.get('X-Request-Id'))
