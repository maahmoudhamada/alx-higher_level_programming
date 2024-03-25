#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    t1, t2 = tuple_a, tuple_b
    a1 = (t1[0], 0) if len(t1) == 1 else (0, 0) if len(t1) == 0 \
        else (t1[0], t1[1])
    a2 = (t2[0], 0) if len(t2) == 1 else (0, 0) if len(t2) == 0 \
        else (t2[0], t2[1])

    out = (a1[0] + a2[0], a1[1] + a2[1])
    return out
