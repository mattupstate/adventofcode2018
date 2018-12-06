from aoc2018.data import load_input

def load_polymer():
    return load_input(__file__)[0].strip()

def react(polymer):
    reacted_polymer = []

    for current_unit in polymer:
        try:
            prev_unit = reacted_polymer.pop()
        except IndexError:
            prev_unit = None

        if prev_unit is None:
            reacted_polymer.append(current_unit)
        elif prev_unit.lower() != current_unit.lower() or prev_unit == current_unit:
            reacted_polymer.append(prev_unit)
            reacted_polymer.append(current_unit)

    return reacted_polymer

def main():
    print(len(react(load_polymer())))

if __name__ == "__main__":
    main()

