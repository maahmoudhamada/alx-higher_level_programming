#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def getfunc(op):
    ops = ['+', '-', '*', '/']
    funcs = [add, sub, mul, div]

    for x in range(len(ops)):
        if op == ops[x]:
            return funcs[x]

    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)


if __name__ == '__main__':
    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a, op, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    func = getfunc(op)
    print("{} {} {} = {}".format(a, op, b, func(a, b)))
