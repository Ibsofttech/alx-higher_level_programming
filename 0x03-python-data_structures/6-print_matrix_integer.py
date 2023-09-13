#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in range(len(matrix)):
        for num in range(len(matrix[r])):
            if num != 0:
                print(" ", end='')
            print("{:d}".format(matrix[r][num]), end='')
        print()
