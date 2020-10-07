#!/usr/bin/python3
"""Defines write_file"""


def write_file(filename="", text=""):
    """Writes string to text file, returns number of chars written"""
    with open(filename) as f:
        f.write(text)
