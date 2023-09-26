#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for elements in my_list:
        if i < x:
            try:
                print(f"{elements}", end='')
                i = i + 1
            except IndexError:
                break
    print()
    return i
