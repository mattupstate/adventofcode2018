import string

from operator import itemgetter

from aoc2018.data import load_input

def parse_instruction(instruction):
    return ''.join([instruction[5], instruction[36]])

def load_instructions():
    return map(parse_instruction, load_input(__file__))


def build_graph(instructions):
    graph = {}

    for dep, target in instructions:
        graph.setdefault(target, set())
        graph[target].add(dep)
        graph.setdefault(dep, set())

    return graph

def follow(graph):
    rv = ""

    while len(graph.keys()) > 0:
        sorted_keys = sorted(graph.keys())

        sorted_items = [(key, graph[key])
                        for key in sorted_keys
                        if len(graph[key]) == 0]

        current, _ = min(sorted_items, key=itemgetter(0))

        rv += current

        del graph[current]

        for _, deps in graph.items():
            if current in deps:
                deps.remove(current)

    print(rv)


def main():
    follow(build_graph(load_instructions()))


if __name__ == "__main__":
    main()
