#!/usr/bin/python3
""" module that adds all args to a list """
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


try:
    args_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    args_list = []

for args in sys.argv[1:]:
    args_list.append(args)
save_to_json_file(args_list, "add_item.json")
