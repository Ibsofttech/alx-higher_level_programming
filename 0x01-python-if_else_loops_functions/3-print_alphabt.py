#!/usr/bin/python3
# alphabets except q and e
for alpha in range(97, 123):
    if (alpha != 113) and (alpha != 101):
        print("{}".format(chr(alpha)), end='')
