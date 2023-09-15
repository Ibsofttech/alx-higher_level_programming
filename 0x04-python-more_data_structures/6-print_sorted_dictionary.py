#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order = list(a_dictionary)
    order.sort()
    for i in order:
        print(f"{i}: {a_dictionary.get(i)}")
