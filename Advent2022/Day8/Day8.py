from typing import Optional

import aoc_utils as au

Map = list[list[str]]


def is_visible(map: Map, x: int, y: int) -> bool:

    return (
        x == 0
        or y == 0
        or x == len(map[0]) - 1
        or y == len(map) - 1
        or all(map[y][x1] < map[y][x] for x1 in range(x))
        or all(map[y][x1] < map[y][x] for x1 in range(x + 1, len(map[0])))
        or all(map[y1][x] < map[y][x] for y1 in range(y))
        or all(map[y1][x] < map[y][x] for y1 in range(y + 1, len(map)))
    )


def test_one(map: Map) -> Optional[int]:

    return sum(
        [
            sum([1 for x in range(len(map[0])) if is_visible(map, x, y)])
            for y in range(len(map))
        ]
    )


def part_one(map: Map) -> Optional[int]:
    return sum(
        [
            sum([1 for x in range(len(map[0])) if is_visible(map, x, y)])
            for y in range(len(map))
        ]
    )


def scenic_score(map: Map, x: int, y: int) -> int:
    sc1 = 0
    x1 = x - 1
    while x1 >= 0:
        sc1 += 1
        if map[y][x1] >= map[y][x]:
            break
        x1 -= 1

    sc2 = 0
    x1 = x + 1
    while x1 < len(map[0]):
        sc2 += 1
        if map[y][x1] >= map[y][x]:
            break
        x1 += 1

    sc3 = 0
    y1 = y - 1
    while y1 >= 0:
        sc3 += 1
        if map[y1][x] >= map[y][x]:
            break
        y1 -= 1

    sc4 = 0
    y1 = y + 1
    while y1 < len(map):
        sc4 += 1
        if map[y1][x] >= map[y][x]:
            break
        y1 += 1
    return sc1 * sc2 * sc3 * sc4


def test_two(map: Map) -> Optional[int]:
    return max(
        [
            max([scenic_score(map, x, y) for x in range(len(map[0]))])
            for y in range(len(map))
        ]
    )


def part_two(map: Map) -> Optional[int]:
    return max(
        [
            max([scenic_score(map, x, y) for x in range(len(map[0]))])
            for y in range(len(map))
        ]
    )


if __name__ == "__main__":
    day = au.Day(
        2022,
        8,
        test_one,
        test_two,
        part_one,
        part_two,
        input=au.MapParser(integer=True),
        test_input=au.MapParser(integer=True),
    )

    day.run_all(run_tests=True)
