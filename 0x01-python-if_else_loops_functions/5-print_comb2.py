#!/usr/bin/python3
for dgt in range(100):
    print("{:02d}".format(dgt), end=(", " if dgt < 99 else "\n"))

