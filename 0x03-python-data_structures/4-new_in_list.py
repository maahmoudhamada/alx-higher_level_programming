#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    lst_cpy = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return lst_cpy
    for x in range(len(lst_cpy)):
        if x == idx:
            lst_cpy[x] = element
    return lst_cpy
