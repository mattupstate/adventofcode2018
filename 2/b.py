import difflib
import itertools
import sys
from a import load_input

def get_different_indexes(a, b):
    return [i for i, char in enumerate(a) if char != b[i]]

def find_off_by_one_char(input):
    for a, b in itertools.product(input[:len(input) -2], input[1:]):
        different_indexes = get_different_indexes(a, b)
        if len(different_indexes) == 1:
            index = different_indexes[0];
            return a[:index] + a[index + 1:]

def main(filename):
    print(find_off_by_one_char(load_input(filename)))

if __name__ == "__main__":
    main(sys.argv[1])
