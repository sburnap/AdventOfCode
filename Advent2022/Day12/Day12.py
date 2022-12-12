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


WalkTest = Callable[[str, str], bool]


class DikjstraData:
    def __init__(self, width: int, height: int):
        self.data: list[list[Optional[int]]] = [
            [None for _ in range(width)] for _ in range(height)
        ]

    def get(self, x: int, y: int) -> Optional[int]:
        return self.data[y][x]

    def set(self, x: int, y: int, val: int):
        self.data[y][x] = val


def dijstra(
    map: Map, start: Position, target: str, can_walk: WalkTest
) -> Optional[int]:
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
                dij[adj.y][adj.x] = dij[work.y][work.x] + 1
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


def true_height(height: str) -> str:
    match height:
        case "S":
            return "a"
        case "E":
            return "z"
        case _:
            return height


def can_walk_up(first: str, second: str) -> bool:
    return ord(true_height(first)) + 1 >= ord(true_height(second))


def test_one(map: Map) -> Optional[int]:
    return dijstra(map, find_start(map, "S"), "E", can_walk_up)


def part_one(map: Map) -> Optional[int]:
    return dijstra(map, find_start(map, "S"), "E", can_walk_up)


def can_walk_down(first: str, second: str) -> bool:
    return ord(true_height(second)) + 1 >= ord(true_height(first))


def test_two(map: Map) -> Optional[int]:
    return dijstra(map, find_start(map, "E"), "a", can_walk_down)


def part_two(map: Map) -> Optional[int]:
    return dijstra(map, find_start(map, "E"), "a", can_walk_down)


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
