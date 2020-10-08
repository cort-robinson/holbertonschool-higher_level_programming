#!/usr/bin/python3
"""Defines pascal_triangle"""


def pascal_triangle(n):
    for i in range(n):
        r = []
        l = len(r)
        r = [1 if i == 0 or i == l else r[i-1]+r[i] for i in range(l + 1)]
        yield r
