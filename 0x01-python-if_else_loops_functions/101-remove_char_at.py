#!/usr/bin/python3

def remove_char_at(str, n):

    out = ""
    for c in range(len(str)):
        if c == n:
            continue
        out += str[c]
    return out
