from aoc2018.data import load_input

def load_polymer():
    return load_input(__file__)[0].strip()

def react(polymer):
    done = False
    while not done:
        start_len = len(polymer)
        for i, c1 in enumerate(polymer[:-1]):
            c2 = polymer[i + 1]
            if (c1.isupper() and c2.islower() and c1.lower() == c2.lower() or
                c1.islower() and c2.isupper() and c1.lower() == c2.lower()):
                polymer = polymer[:i] + polymer[i+2:]
                break
        done = start_len == len(polymer)
    return polymer

def main():
    print(len(react(load_polymer())))

if __name__ == "__main__":
    main()

