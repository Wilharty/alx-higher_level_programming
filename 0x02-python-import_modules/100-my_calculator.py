#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    arg_number = len(argv) - 1
    if arg_number != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if argv[2] not in {"+", "-", "*", "/"}:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            operator = {"+": add, "-": sub, "*": mul, "/": div}
            a = int(argv[1])
            b = int(argv[3])
            print(f"{a} {argv[2]} {b} = {operator[argv[2]](a, b)}")
