#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(valur))
    except ValueError:
        print("invalid input.Please put an integer")
