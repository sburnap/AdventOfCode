import aoc_utils as au
from itertools import permutations


def get_distances(input: str) -> dict:
    distances = {}

    for source, destination, distance in input:
        distances.setdefault(source, {})[destination] = distance
        distances.setdefault(destination, {})[source] = distance

    return distances


def get_route_lengths(distances: dict):
    for route in permutations(distances.keys()):
        yield sum([distances[route[i]][route[i + 1]] for i in range(len(route) - 1)])


def find_min_route(distances: dict) -> int:
    return min(get_route_lengths(distances))


def find_max_route(distances: dict) -> int:
    return max(get_route_lengths(distances))


def test_one(input: str) -> int:
    return find_min_route(get_distances(input))


# expected 251
def part_one(input: list[str]) -> int:
    return find_min_route(get_distances(input))


def test_two(input: str) -> int:
    return find_max_route(get_distances(input))


# expected 898
def part_two(input: list[str]) -> int:
    return find_max_route(get_distances(input))


if __name__ == "__main__":
    distance_parser = au.RegexParser(
        [("(.*) to (.*) = (.*)", lambda x: (x[0], x[1], int(x[2])))]
    )
    day = au.Day(
        2015,
        9,
        test_one,
        test_two,
        part_one,
        part_two,
        input=distance_parser,
        test_input=distance_parser,
    )

    day.run_all(run_tests=True)
