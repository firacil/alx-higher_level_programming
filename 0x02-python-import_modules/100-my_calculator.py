#!/usr/bin/python3
"""program to import all functions from the file calcluator_1.py"""
if __name__ == "__main__":
    """ implements arthimatic operation"""
    from calculator_1 import add, sub, mul, div
    import sys

    argument_number = len(sys.argv) - 1

    opr = {"+": add, "*": mul, "-": sub, "/": div}

    if argument_number != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        if sys.argv[2] not in list(opr.keys()):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print("{} {} {} = {}".format(a, sys.argv[2], b, opr[sys.argv[2]](a, b)))
