#!/usr/bin/python3

def uppercase(str):

    for x in str:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            print("{:c}".format(ord(x) - 32), end="")
        else:
            print("{}".format(x), end="")
    print()
