#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[:2] + (0, 0)[len(tuple_a[:2]):]
    b = tuple_b[:2] + (0, 0)[len(tuple_b[:2]):]
    return (a[0] + b[0], a[1] + b[1])
