#!/usr/bin/python3
"""Takes URL and displays value of X-Request-Id in header response"""
from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
