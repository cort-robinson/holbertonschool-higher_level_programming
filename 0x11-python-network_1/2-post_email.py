#!/usr/bin/python3
"""sends POST reqsuest to passed URL with email as parameter"""
from sys import argv
from urllib import request
from urllib import parse

if __name__ == "__main__":
    data = parse.urlencode({'email': argv[2]}).encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as f:
        print(f.read().decode('utf-8'))
