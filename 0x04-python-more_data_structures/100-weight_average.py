#!/usr/bin/python3
def weight_average(my_list=[]):
        if not isinstance(my_list, list) or len(my_list) == 0:
            return 0
        size = avg = 0
        for tup in my_list:
            x, y = tup
            size += (x * y)
            avg += y
        return size / avg
