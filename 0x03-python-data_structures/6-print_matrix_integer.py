#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if column < (len(matrix) - 1):
                separator = ' '
            else:
                separator = ''
            print('{:d}'.format(matrix[row][column]), end=separator)
        print()
