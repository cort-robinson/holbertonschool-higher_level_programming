#!/usr/bin/python3
def remove_char_at(str, n):
    strout = ""
    for i in range(len(str)):
        if i != n:
            strout += str[i]
    return strout
