#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    nb = 0
    try:
        for y in range(x):
            print("{}".format(my_list[y]), end="")
            nb += 1
    except IndexError:
        pass
    finally:
        print()
    return nb
