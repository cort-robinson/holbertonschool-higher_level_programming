#!/usr/bin/python3
"""contains find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    if len(list_of_integers) < 2:
        return list_of_integers[0]

    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]
    for _ in range(len(list_of_integers)):
        if list_of_integers[_] > list_of_integers[_ - 1] \
                and list_of_integers[_] > list_of_integers[_ + 1]:
            return list_of_integers[_]
