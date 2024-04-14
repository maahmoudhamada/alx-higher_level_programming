#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

my_dict = { 'a': 4, 'b': 3, 'c': 5, 'd': 1, 'e': 2 }
best_key = best_score(my_dict)
print("Best: {}".format(best_key))
