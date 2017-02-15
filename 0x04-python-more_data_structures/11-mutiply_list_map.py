#!/usr/bin/python3
def mul(x, y):
    return x * y

def mutiply_list_map(my_list=[], number=0):
    if len(my_list) is 0:
        return

    new_list = list(map(lambda x: x * number, my_list))

    return new_list
