#!/usr/bin/python3

def multiple_returns(sentence):

    sz = len(sentence)
    if sz == 0:
        return (sz, None)
    else:
        return (sz, sentence[0])
