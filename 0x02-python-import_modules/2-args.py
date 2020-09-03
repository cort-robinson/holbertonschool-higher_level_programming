#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argcount = len(argv) - 1
    if argcount == 1:
        print("{:d} argument:".format(argcount))
    elif argcount == 0:
        print("{:d} arguments.".format(argcount))
    else:
        print("{:d} arguments:".format(argcount))
    if argcount > 0:
        i = 1
        while i <= argcount:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1
