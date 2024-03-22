#!/usr/bin/python3

def fizzbuzz():
    for x in range(1, 101):

        if not x % 3 and not x % 5:
            print("FizzBuzz", end=" ")
        elif not x % 3:
            print("Fizz", end=" ")
        elif not x % 5:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(x), end=" ")
