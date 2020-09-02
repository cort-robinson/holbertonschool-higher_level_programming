#!/usr/bin/python3
def uppercase(str):
    strout = ""
    for i in str:
        i = ord(i)
        if 97 <= i <= 122:
            i -= 32
        strout += chr(i)
    print("{:s}".format(strout))