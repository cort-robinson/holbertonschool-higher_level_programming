#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    i = 1
    sum = 0
    while i <= len(argv) - 1:
        sum += int(argv[i])
        i += 1
    print("{:d}".format(sum))
