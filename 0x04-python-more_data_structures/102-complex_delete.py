#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = {k: v for k, v in a_dictionary.items() if v != value}
    a_dictionary.clear()
    a_dictionary.update(tmp)
    return a_dictionary
