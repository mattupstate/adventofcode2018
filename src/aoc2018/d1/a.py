import os
import sys

from aoc2018.data import load_input

def map_strings_to_ints(deltas):
    return list(map(int, deltas))

def reduce_frequencies(deltas):
    frequency = 0
    for delta in deltas:
        frequency += delta
    return frequency

def load_deltas():
    return map_strings_to_ints(load_input(__file__))

def __main__():
    print(reduce_frequencies(load_deltas()))

if __name__ == "__main__":
    __main__()
