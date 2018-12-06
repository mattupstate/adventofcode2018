from aoc2018.d6.a import load_coordinates, manhattan_distance, Coordinate

def main():
    coordinates, max_x, max_y = load_coordinates()
    tally = 0
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            distance = 0
            for coord in coordinates:
                distance += manhattan_distance(Coordinate(x, y), coord)
            if distance < 10000:
                tally += 1
    print(tally)

if __name__ == "__main__":
    main()
