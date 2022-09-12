#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    list_len = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            list_len += 1
        except IndexError:
            break
    print()
    return list_len
