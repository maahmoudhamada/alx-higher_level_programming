#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    kys = [x for x in a_dictionary.keys()]
    for x in sorted(kys):
        print("{}: {}".format(x, a_dictionary[x]))
