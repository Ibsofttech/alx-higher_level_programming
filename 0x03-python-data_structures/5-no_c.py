#!/usr/bin/python3
def no_c(my_string):
    my_2_str = []
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            my_2_str.append(ch)
    return ''.join(my_2_str)
