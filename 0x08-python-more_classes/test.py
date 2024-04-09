#!/usr/bin/python3

class A:

    @staticmethod
    def bigger_or_equal(rect_1):
        if rect_1.__class__ is not A:
            raise TypeError("ay haga")
        else:
            print("Correct")


x = 7
A.bigger_or_equal(x)
