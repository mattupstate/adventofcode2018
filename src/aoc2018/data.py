import os

def load_input(base, filename='input.txt'):
    with open(relative_path(base, filename)) as f:
        return f.readlines()

def relative_path(base, filename):
    return os.path.join(os.path.dirname(base), filename)
