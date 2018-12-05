import sys

from collections import Counter

from aoc2018.data import load_input

def count_exact_occurences_of_characters(strings, occurences):
    rv = {o: 0 for o in occurences}

    for string in strings:
        counter = set(Counter(string).values())
        for o in occurences:
            if o in counter:
                rv[o] += 1

    return rv

def calculate_checksum(identifiers, occurences):
    occurences = count_exact_occurences_of_characters(identifiers, occurences)
    result = 1
    for count in occurences.values():
        result = result * count
    return result

def load_identifiers():
    return load_input(__file__)

def main():
    print(calculate_checksum(load_identifiers(), [3, 2]))

if __name__ == "__main__":
    main()
