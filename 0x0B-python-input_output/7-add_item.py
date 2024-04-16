#!/usr/bin/python3

"""The add_item Module adds all arguments to a Python list
and then save them to a file"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argvList = []
filename = 'add_item.json'
argvList = [sys.argv[x] for x in range(1, len(sys.argv))]
try:
    jsonString = load_from_json_file(filename)
except Exception:
    jsonString = []

jsonString += argvList
save_to_json_file(jsonString, filename)
