#!/usr/bin/python3
def islower(c):
   """funct that checks for lowercase characters"""
    c = ord(c)
        if (c >= 97 and c <= 122):
            return True
        else:
            return False
