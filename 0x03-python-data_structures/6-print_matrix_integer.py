#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''function that prints a matrix of integers'''
    for lignes in matrix:
        for entiers in lignes:
            print("{}".format(entiers, end = ' '))
        print()
