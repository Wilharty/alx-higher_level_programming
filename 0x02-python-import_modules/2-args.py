#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number = len(argv) - 1
    if number == 0:
        print("0 argument.")
    else:
        if number == 1:
            print("1 argument:")
        elif number > 1:
            print("{} arguments:".format(number))
        for i in range(1, number + 1):
            print("{}: {}".format(i, argv[i]))
