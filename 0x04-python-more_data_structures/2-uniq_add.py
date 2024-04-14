#!/usr/bin/python3

def uniq_add(my_list=[]):

    sum = 0
    st = {x for x in my_list}

    for x in st:
        sum += x
    return sum
