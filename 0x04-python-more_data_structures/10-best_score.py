#!/usr/bin/python3
def best_score(a_dictionary):
    largest = 0
    largest_key = None
    if a_dictionary is not None:
        for key, value in a_dictionary.items():
            if value > largest:
                largest = value
                largest_key = key
    return largest_key
