#!/usr/bin/python3

x = dir(hidden_4)
for i in x:
    if i[0] is not '_':
        continue
    else:
        print(i)
