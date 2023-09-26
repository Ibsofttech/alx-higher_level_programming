#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for elem in range(0, x):
        try:
            print("{:d}".format(my_list[elem]), end="")
            i = i + 1
        except (TypeError, ValueError):
            continue
    print()
    return i
