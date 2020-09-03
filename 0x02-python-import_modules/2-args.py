#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argcount = len(argv) - 1
    print("{:d} argument".format(argcount), end="")
    if argcount != 1:
        print("s." if argcount == 0 else "s")
    else:
        print(":")
    if argcount > 0:
        i = 1
        while i <= argcount:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1
