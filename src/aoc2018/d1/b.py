import operator
import os
import sys

from aoc2018.d1.a import load_deltas

def find_first_repeated_frequency(deltas):
    frequency = 0
    frequencies = set([frequency])
    while True:
        for delta in deltas:
            frequency += delta
            if frequency in frequencies:
                return frequency
            frequencies.add(frequency)

def __main__():
    print(find_first_repeated_frequency(load_deltas()))

if __name__ == "__main__":
    __main__()
