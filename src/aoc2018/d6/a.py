from collections import namedtuple
from operator import itemgetter

from aoc2018.data import load_input

Coordinate = namedtuple('Coordinate', ['x', 'y'])

def manhattan_distance(c1, c2):
    return abs(c1.x - c2.x) + abs(c1.y - c2.y)

def load_coordinates():
    coordinates = list(map(lambda i: Coordinate(*[int(p) for p in i]),
        map(lambda i: i.strip().split(", "), load_input(__file__))))
    max_x, _ = max(coordinates, key=itemgetter(0))
    _, max_y = max(coordinates, key=itemgetter(1))
    return coordinates, max_x, max_y


def main():
    coordinates, max_x, max_y = load_coordinates()
    tallies = {coord: (0, False) for coord in coordinates}

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            closest_coords = []
            closest_coord_distance = max_x * max_y

            for coord in coordinates:
                distance = manhattan_distance(Coordinate(x, y), coord)

                if distance < closest_coord_distance:
                    closest_coords = [coord]
                    closest_coord_distance = distance
                elif distance == closest_coord_distance:
                    closest_coords.append(coord)

            if len(closest_coords) == 1:
                tally, is_infinite = tallies[closest_coords[0]]

                if not is_infinite and x == 0 or x == max_x or y == 0 or y == max_y:
                    is_infinite = True

                tally += 1
                tallies[closest_coords[0]] = (tally, is_infinite)

    for tally, is_infinite in sorted(tallies.values(), key=itemgetter(0), reverse=True):
        if not is_infinite:
            print(tally)
            break

if __name__ == "__main__":
    main()
