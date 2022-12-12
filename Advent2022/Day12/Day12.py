from typing import Optional, Generator, Callable
from dataclasses import dataclass

import aoc_utils as au

Map = list[list[str]]


@dataclass
class Position:
    x: int
    y: int


def adjacent(position: Position, map: Map) -> Generator[Position, None, None]:
    if position.x > 0:
        yield Position(position.x - 1, position.y)
    if position.y > 0:
        yield Position(position.x, position.y - 1)

    if position.x < len(map[0]) - 1:
        yield Position(position.x + 1, position.y)
    if position.y < len(map) - 1:
        yield Position(position.x, position.y + 1)


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


WalkTest = Callable[[str, str], bool]


def dijstra(map: Map, start: Position, target: str, can_walk: WalkTest) -> int:
    dij: list[list[Optional[int]]] = [
        [None for _ in range(len(map[0]))] for _ in range(len(map))
    ]

    dij[start.y][start.x] = 0
    work_queue: list[Position] = [start]

    while len(work_queue) > 0:
        work = work_queue.pop(0)
        for adj in adjacent(work, map):
            if dij[adj.y][adj.x] is None and can_walk(
                map[work.y][work.x], map[adj.y][adj.x]
            ):
                steps = dij[work.y][work.x]
                dij[adj.y][adj.x] = steps + 1 if steps is not None else 0
                work_queue.append(Position(adj.x, adj.y))
                if map[adj.y][adj.x] == target:
                    return dij[adj.y][adj.x]

    return 0


def find_start(map: Map, start: str) -> Position:
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == start:
                return Position(x, y)

    raise Exception("No starting position found")


def can_walk_up(first: str, second: str) -> bool:
    if first == "S":
        first = "a"
    if second == "E":
        second = "z"
    return ord(first) + 1 >= ord(second)


def test_one(map: Map) -> Optional[int]:
    start = find_start(map, "S")

    return dijstra(map, start, "E", can_walk_up)


def part_one(map: Map) -> Optional[int]:
    start = find_start(map, "S")

    return dijstra(map, start, "E", can_walk_up)


def can_walk_down(first: str, second: str) -> bool:
    if first == "E":
        first = "z"
    if second == "S":
        second = "a"
    return ord(second) +1 >= ord(first) 


def test_two(map: Map) -> Optional[int]:
    start = find_start(map, "E")

    return dijstra(map, start, "a", can_walk_down)


def part_two(map: Map) -> Optional[int]:
    start = find_start(map, "E")

    return dijstra(map, start, "a", can_walk_down)


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
