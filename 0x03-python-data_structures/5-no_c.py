#!/usr/bin/python3

def no_c(my_string):

    str_cpy = ''
    for x in my_string:
        if x == 'c' or x == 'C':
            continue
        str_cpy += x
    return str_cpy
