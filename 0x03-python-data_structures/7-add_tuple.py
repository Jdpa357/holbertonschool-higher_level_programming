#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) or len(tuple_b) < 2:
        for i in range(2):
            tuple_a = tuple_a + (0,)
            tuple_b = tuple_b + (0,)
    tuple_a = (tuple_a[0], tuple_a[1])
    tuple_b = (tuple_b[0], tuple_b[1])
    result_a = tuple_a[0] + tuple_b[0]
    result_b = tuple_a[1] + tuple_b[1]
    total_result = (result_a, result_b)
    return total_result
