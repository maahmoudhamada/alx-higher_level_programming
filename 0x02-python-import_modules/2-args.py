#!/usr/bin/python3

import sys

if __name__ == '__main__':
    argc = len(sys.argv) - 1
    args = 'argument' if argc == 1 else 'arguments'
    args += '.' if argc == 0 else ':'
    print("{} {}".format(argc, args))
    for x in range(1, len(sys.argv)):
        print("{}: {}".format(x, sys.argv[x]))
