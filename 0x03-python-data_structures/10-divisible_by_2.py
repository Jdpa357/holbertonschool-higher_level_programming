#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    working_list = []
    for i in my_list:
        if not i % 2:
            working_list.append(True)
        else:
            working_list.append(False)
    return working_list
