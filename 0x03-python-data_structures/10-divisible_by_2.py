#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    retList = []
    for i in my_list:
        if i % 2 == 0:
            retList += [True]
        else:
            retList += [False]
    return retList
