#!/usr/bin/python3
def fizzbuzz():
    for val in range(1, 101):
        if val % 3 == 0 and val % 5 == 0:
            print(f"FizzBuzz ", end='')
        elif val % 3 == 0:
            print(f"Fizz ", end='')
        elif val % 5 == 0:
            print(f"Buzz ", end='')
        else:
            print(f"{dgt} ", end='')
