#!/usr/bin/python3
def max_integer(my_list=[]):
    new_list = len(my_list)

    if new_list == 0:
        return None

    max_int = my_list[0]

    for i in range(1, new_list):
        if my_list[i] > max_int:
            max_int = my_list[i]

    return (max_int)
