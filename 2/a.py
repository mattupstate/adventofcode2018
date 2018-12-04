import sys
from collections import Counter

def calculate_checksum(input, occurences):
    d = {o: 0 for o in occurences}

    for item in input:
        counter = set(Counter(item).values())
        for o in occurences:
            if o in counter:
                d[o] += 1

    return reduce(lambda x, y: x * y, d.values())

def load_input(filename):
    with open(filename) as f:
        return f.readlines()

def main(filename):
    print(calculate_checksum(load_input(filename), [3, 2]))

if __name__ == "__main__":
    main(sys.argv[1])
