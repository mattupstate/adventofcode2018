from aoc2018.d3.a import load_claims, get_grid

def main():
    claims = load_claims()
    for a in claims:
        intersects = False
        for b in claims:
            if a == b:
                continue
            if len(get_grid(a, 1000, 1000) & get_grid(b, 1000, 1000)) > 0:
                intersects = True
                break
        if not intersects:
            print(a.id)
            return

if __name__ == "__main__":
    main()
