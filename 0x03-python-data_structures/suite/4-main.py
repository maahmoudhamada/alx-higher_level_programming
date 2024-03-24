#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

list = [1]
idx = 0
element = 4
new_list = new_in_list(list, idx, element)

print(new_list)
print(list)
