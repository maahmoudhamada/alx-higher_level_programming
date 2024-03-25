#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    lst = [x % 2 == 0 for x in my_list]
    return lst
