#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None:
        return

    else:
        lst = sorted(a_dictionary.values())
        max = lst[-1]
        for kys, vals in a_dictionary.items():
            if vals == max:
                return kys
