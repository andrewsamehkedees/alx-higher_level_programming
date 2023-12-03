#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 || len(my_list) < idx:
        return :
    else:
        print("Element at index {:d} is {:d}".format(idx, my_list[idx]))
