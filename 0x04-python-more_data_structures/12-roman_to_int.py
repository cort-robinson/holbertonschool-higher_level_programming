#!/usr/bin/python3
def value(n):
    if n == 'I':
        return 1
    if n == 'V':
        return 5
    if n == 'X':
        return 10
    if n == 'L':
        return 50
    if n == 'C':
        return 100
    if n == 'D':
        return 500
    if n == 'M':
        return 1000
    return -1


def roman_to_int(roman_string):
    sum = 0
    for i in range(len(roman_string)):
        current_v = value(roman_string[i])
        if i + 1 < len(roman_string):
            if roman_string[i + 1]:
                next_v = value(roman_string[i + 1])
            if current_v < next_v:
                sum += next_v - current_v
                i += 1
                continue
        sum += current_v
    return sum
