#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(list[i])
    except IndexError:
        print("There are not enough elements in the list to print.")
