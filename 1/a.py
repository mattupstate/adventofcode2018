import operator
import os
import sys

ops = {
    "+": operator.add,
    "-": operator.sub,
}

def eval_integer(value):
    return ops[value[0]](0, int(value[1:]))

def map_strings_to_ints(input):
    return map(eval_integer, input);

def reduce_frequencies(input):
    return reduce(lambda x, y: x + y, input)

def load_input(filename):
    with open(filename) as f:
        return f.readlines()

def main(filename):
    print(reduce_frequencies(map_strings_to_ints(load_input(filename))))

if __name__ == "__main__":
    main(sys.argv[1])
