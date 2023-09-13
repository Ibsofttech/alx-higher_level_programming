#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if idx >= len(my_list) or idx < 0:
        return my_list
    else:
        n_list = my_list[:]
        n_list[idx] = element
        return n_list
