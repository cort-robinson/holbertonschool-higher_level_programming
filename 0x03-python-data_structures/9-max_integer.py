#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    biggestInt = my_list[0]
    for i in my_list:
        if i > biggestInt:
            biggestInt = i
    return biggestInt
