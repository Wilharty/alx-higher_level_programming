#!/usr/bin/python3

"""print the ASCII alphabet, in low, not f by a nl"""
for i in range(97, 123):
   if i != 101 and i!= 113: 
          print("{}".format(chr(i)), end="")
