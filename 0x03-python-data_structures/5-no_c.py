#!/usr/bin/python3
def no_c(my_string):
    working_string = list(my_string)
    working_string = [c for c in working_string if c not in 'cC']
    working_string = ''.join(working_string)
    return working_string
