#!/usr/bin/python3

def uppercase(str):

    for x in str:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            c = ord(x) - 32
        else:
            c = ord(x)
        print("{:c}".format(c), end="")
    print()
