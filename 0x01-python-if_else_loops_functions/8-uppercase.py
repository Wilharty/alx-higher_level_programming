#!/usr/bin/python3
def uppercase(str):
    """funct that prints a str in upper f by a new l"""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end = "")
    print()
