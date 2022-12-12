from typing import Optional, Generator, Callable
from dataclasses import dataclass

import aoc_utils as au


@dataclass
class Position:
    x: int
    y: int


class DikjstraData:
    def __init__(self, width: int, height: int):
        self.data: list[list[Optional[int]]] = [
            [None for _ in range(width)] for _ in range(height)
        ]

    def is_set(self, x: int, y: int) -> bool:
        return self.data[y][x] is not None

    def get(self, x: int, y: int) -> int:
        if (rc := self.data[y][x]) is not None:
            return rc
        raise Exception("Attempt to read unset DikjstraData")

    def set(self, x: int, y: int, val: int):
        self.data[y][x] = val


class Map:
    def __init__(self, data: list[list[str]]):
        self.data = data

    def height(self):
        return len(self.data)

    def width(self):
        return len(self.data[0])

    def get(self, x: int, y: int) -> str:
        return self.data[y][x]

    def set(self, x: int, y: int, val: str):
        self.data[y][x] = val


def adjacent(position: Position, map: Map) -> Generator[Position, None, None]:
    if position.x > 0:
        yield Position(position.x - 1, position.y)
    if position.y > 0:
        yield Position(position.x, position.y - 1)

    if position.x < map.width() - 1:
        yield Position(position.x + 1, position.y)
    if position.y < map.height() - 1:
        yield Position(position.x, position.y + 1)


WalkTest = Callable[[str, str], bool]


def dijstra(
    map: Map, start: Position, target: str, can_walk: WalkTest
) -> Optional[int]:
    dij = DikjstraData(map.width(), map.height())

    dij.set(start.x, start.y, 0)

    work_queue: list[Position] = [start]

    while len(work_queue) > 0:
        work = work_queue.pop(0)
        for adj in adjacent(work, map):
            if not dij.is_set(adj.x, adj.y) and can_walk(
                map.get(work.x, work.y), map.get(adj.x, adj.y)
            ):
                dij.set(adj.x, adj.y, dij.get(work.x, work.y) + 1)
                work_queue.append(Position(adj.x, adj.y))
                if map.get(adj.x, adj.y) == target:
                    return dij.get(adj.x, adj.y)

    return 0


def find_start(map: Map, start: str) -> Position:
    for y in range(map.height()):
        for x in range(map.width()):
            if map.get(x, y) == start:
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


def test_one(input: list[list[str]]) -> Optional[int]:
    map = Map(input)
    return dijstra(map, find_start(map, "S"), "E", can_walk_up)


def part_one(input: list[list[str]]) -> Optional[int]:
    map = Map(input)
    return dijstra(map, find_start(map, "S"), "E", can_walk_up)


def can_walk_down(first: str, second: str) -> bool:
    return ord(true_height(second)) + 1 >= ord(true_height(first))


def test_two(input: list[list[str]]) -> Optional[int]:
    map = Map(input)
    return dijstra(map, find_start(map, "E"), "a", can_walk_down)


def part_two(input: list[list[str]]) -> Optional[int]:
    map = Map(input)
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
