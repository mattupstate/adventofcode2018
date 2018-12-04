import operator
import os
import sys
from a import map_strings_to_ints, load_input

def find_first_repeated_frequency(input):
    frequency = 0
    frequencies = set([frequency])
    while True:
        for delta in input:
            frequency += delta
            if frequency in frequencies:
                return frequency
            frequencies.add(frequency)

def main(filename):
    print(find_first_repeated_frequency(map_strings_to_ints(load_input(filename))))

if __name__ == "__main__":
    main(sys.argv[1])
