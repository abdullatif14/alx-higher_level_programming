#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div = len(my_list)

    for i in range(1, my_list):
        if i % 2 == 0:
            div.append(True)
        else:
            div.append(False)

    return div
