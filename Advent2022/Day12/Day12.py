from typing import Optional, Generator

import aoc_utils as au

Map = list[list[str]]


def adjacent(x: int, y: int, map: Map) -> Generator[tuple[int, int], None, None]:
    if x > 0:
        yield x - 1, y
    if y > 0:
        yield x, y - 1

    if x < len(map[0]) - 1:
        yield x + 1, y
    if y < len(map) - 1:
        yield x, y + 1


def find_start_end(map: Map) -> tuple[tuple[int, int], tuple[int, int]]:
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "S":
                start = (x, y)
                map[y][x] = "a"
            if map[y][x] == "E":
                end = (x, y)
                map[y][x] = "z"

    return start, end


def dijstra(map: Map, start: tuple[int, int], target: tuple[int, int]) -> int:
    dij: list[list[Optional[int]]] = [
        [None for _ in range(len(map[0]))] for _ in range(len(map))
    ]

    startx, starty = start
    dij[starty][startx] = 0

    while True:
        for y in range(len(map)):
            for x in range(len(map[0])):
                if (x, y) == target and dij[y][x] is not None:
                    return dij[y][x]
                for x1, y1 in adjacent(x, y, map):
                    if (
                        dij[y][x] is not None
                        and dij[y1][x1] is None
                        and ord(map[y][x]) + 1 >= ord(map[y1][x1])
                    ):
                        dij[y1][x1] = dij[y][x] + 1


def test_one(map: Map) -> Optional[int]:
    start, target = find_start_end(map)
    return dijstra(map, start, target)


def part_one(map: Map) -> Optional[int]:
    start, target = find_start_end(map)
    return dijstra(map, start, target)


def dijstra2(map: Map, start: tuple[int, int]) -> int:
    dij: list[list[Optional[int]]] = [
        [None for _ in range(len(map[0]))] for _ in range(len(map))
    ]

    startx, starty = start
    dij[starty][startx] = 0

    done = False
    while not done:
        done = True
        for y in range(len(map)):
            for x in range(len(map[0])):
                for x1, y1 in adjacent(x, y, map):
                    if (
                        dij[y][x] is not None
                        and dij[y1][x1] is None
                        and ord(map[y1][x1]) + 1 >= ord(map[y][x])
                    ):
                        dij[y1][x1] = dij[y][x] + 1
                        done = False

    mn = 9999
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "a" and dij[y][x] is not None and dij[y][x] < mn:
                mn = dij[y][x]

    return mn


def test_two(map: Map) -> Optional[int]:
    _, target = find_start_end(map)
    return dijstra2(map, target)


def part_two(map: Map) -> Optional[int]:
    _, target = find_start_end(map)
    return dijstra2(map, target)


if __name__ == "__main__":
    day = au.Day(
        2022,
        12,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=au.MapParser(),
        input=au.MapParser(),
    )

    day.run_all(run_tests=True)
