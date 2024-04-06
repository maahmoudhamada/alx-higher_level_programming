#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    res = None
    try:
        res = fct(args[0], args[1])
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return res
