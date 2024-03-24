#!/usr/bin/python3

import sys
argc = len(sys.argv)

arg = "arguement" if argc - 1 == 1 else "arguments"
arg += '.' if argc - 1 == 0 else ':'
print("{:d} {}".format(argc - 1, arg))
for x in range(1, argc):
    print("{:d} {}".format(x, sys.argv[x]))
