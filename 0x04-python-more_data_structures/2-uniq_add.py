#!/usr/bin/python3

lst = [1, 2, 3, 1, 4, 2, 5]

l1 = [x for x in lst if lst.count(x) == 1   ]
print(l1)
