#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Return a new modified list by replacing search's value
    by replace's value
    """
    return [x if x != search else replace for x in my_list]
