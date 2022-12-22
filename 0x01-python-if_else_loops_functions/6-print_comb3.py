#!/usr/bin/python3
"""print all possible different combinations of two digits"""
for i in range(0, 9):
    for j in range(i + 1, 10):
        if i + j != 17:
            print("{}{}".format(i, j), end = ", ")
        else:
            print("{}{}".format(i, j), end = "")
