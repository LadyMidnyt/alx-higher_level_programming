#!/usr/bin/python3
<<<<<<< HEAD
# 6-print_matrix_integer.py
# Brennan D Baraban <375@holbertonschool.com>

=======
>>>>>>> 135b120004f2d3c2dad96982f601b2973ae6e36f

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                print("{:d}".format(matrix[i][j]), end="")
                if j != (len(matrix[i]) - 1):
                    print(" ", end="")

        print("")
