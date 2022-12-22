#!/usr/bin/python3

"""print the ASCII alphabet, in rev order, alternating low and upper, f by a nl
   Expl: z in lowercase and Y in uppercase"""
for i in range(122, 96, -1):
    if i % 2 != 0:
        print("{:c}".format(i - 32), end='')
    else:
        print("{:c}".format(i), end='')
