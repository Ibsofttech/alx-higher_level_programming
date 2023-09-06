#!/usr/bin/python3
def remove_char_at(str, my_n):
    if my_n < 0:
        return (str)
    return (str[:my_n] + str[my_n+1:])
