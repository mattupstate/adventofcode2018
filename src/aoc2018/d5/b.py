import string

from aoc2018.d5.a import load_polymer, react

def main():
    polymer = load_polymer()

    most_problematic_unit = None
    polymer_length = len(polymer)

    for unit in string.ascii_lowercase:
        modified_polymer = polymer.replace(unit, "").replace(unit.upper(), "")
        reacted_polymer = react(modified_polymer)
        reacted_polymer_length = len(reacted_polymer)

        if reacted_polymer_length < polymer_length:
            most_problematic_unit = unit
            polymer_length = reacted_polymer_length

    print(most_problematic_unit, polymer_length)

if __name__ == "__main__":
    main()
