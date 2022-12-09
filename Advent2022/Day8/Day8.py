from typing import Optional, Generator

import aoc_utils as au

Map = list[list[int]]


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


# expect 21
def test_one(map: Map) -> Optional[int]:

    return sum(
        [
            sum([1 for x in range(len(map[0])) if is_visible(map, x, y)])
            for y in range(len(map))
        ]
    )


# expect 1708
def part_one(map: Map) -> Optional[int]:
    return sum(
        [
            sum([1 for x in range(len(map[0])) if is_visible(map, x, y)])
            for y in range(len(map))
        ]
    )


def visible_line(trees: list[int], height: int) -> Generator[int, None, None]:

    for tree in trees:
        yield tree
        if height <= tree:
            break


def scenic_score(map: Map, x: int, y: int) -> int:
    height = map[y][x]
    return (
        len(list(visible_line([map[y][x1] for x1 in range(x - 1, -1, -1)], height)))
        * len(
            list(visible_line([map[y][x1] for x1 in range(x + 1, len(map[0]))], height))
        )
        * len(list(visible_line([map[y1][x] for y1 in range(y - 1, -1, -1)], height)))
        * len(
            list(visible_line([map[y1][x] for y1 in range(y + 1, len(map[0]))], height))
        )
    )


# expect 8
def test_two(map: Map) -> Optional[int]:
    return max(
        [
            max([scenic_score(map, x, y) for x in range(len(map[0]))])
            for y in range(len(map))
        ]
    )


# expect 504000
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
