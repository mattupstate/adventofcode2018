import difflib
import itertools
import sys

from aoc2018.d2.a import load_identifiers

def get_different_indexes(a, b):
    return [i for i, char in enumerate(a) if char != b[i]]

def find_off_by_one_char(input):
    for a, b in [(a, b) for a in input for b in input]:
        different_indexes = get_different_indexes(a, b)
        if len(different_indexes) == 1:
            index = different_indexes[0]
            return a[:index] + a[index + 1:]

def main():
    print(find_off_by_one_char(load_identifiers()))

if __name__ == "__main__":
    main()
