#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    items = len(my_list)

    new_list = my_list.copy()

    if idx < 0 > items:
        return my_list

    new_list[idx] = element
    return new_list
