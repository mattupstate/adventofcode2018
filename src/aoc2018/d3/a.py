import itertools
import sys

from collections import namedtuple

from aoc2018.data import load_input

GRIDS = dict()

class Claim(object):
    def __init__(self, id, x, y, width, height):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def parse_claim(value):
    id, parts = value.strip().split(' @ ')
    position, dimensions = parts.split(': ')
    x, y = position.split(',')
    width, height = dimensions.split('x')
    return Claim(id, int(x), int(y), int(width), int(height))

def generate_grid(claim, canvas_width, canvas_height):
    canvas_width = canvas_width or claim.width
    canvas_height = canvas_height or claim.height
    return set([canvas_width * (claim.y + r) + claim.x + c for r in range(claim.height) for c in range(claim.width)])

def get_grid(claim, canvas_width, canvas_height):
    if claim.id not in GRIDS:
        GRIDS[claim.id] = generate_grid(claim, canvas_width, canvas_height)
    return GRIDS[claim.id]

def load_claims():
    return list(map(parse_claim, load_input(__file__)))

def main():
    claims = load_claims()
    result = set()
    for a, b in [(a, b) for a in claims for b in claims if a != b]:
        result.update(get_grid(a, 1000, 1000) & get_grid(b, 1000, 1000))
    print(len(result))

if __name__ == "__main__":
    main()
