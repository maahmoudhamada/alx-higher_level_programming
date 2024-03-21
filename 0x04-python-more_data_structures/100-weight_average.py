#!/usr/bin/python3

def weight_average(my_list=[]):
    sum1 = sum2 = 0

    for x, y in my_list:
        sum1 += x * y
        sum2 += y
    return sum1 / sum2
