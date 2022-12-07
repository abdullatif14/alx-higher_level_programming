#!/usr/bin/python3
def no_c(my_string):
    chars = len(my_string)
    new_string = ""
    for i in range(0, chars):
        if my_string[i] == "c" or my_string[i] == "C":
            continue
        new_string = new_string + my_string[i]

    return new_string
