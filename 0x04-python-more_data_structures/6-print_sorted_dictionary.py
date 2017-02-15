#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    #sorted(my_dict.keys())

    for i, j in sorted(my_dict.items()):
        print("{:s}: {}".format(i, j))
