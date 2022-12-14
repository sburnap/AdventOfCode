from typing import Optional
from dataclasses import dataclass

import aoc_utils as au


@dataclass
class Point:
    x: int
    y: int


class Map:
    def __init__(self, input: list[list[Point]], showmap=False):
        self.showmap = showmap

        maxy = max(max(a.y for a in line) for line in input) + 2
        minx = min(min(a.x for a in line) for line in input) - maxy
        maxx = max(max(a.x for a in line) for line in input) + maxy

        self.offset = minx
        width = (maxx - minx) + 1
        self.data = [["." for _ in range(width)] for _ in range(maxy + 1)]

        self.update_rock_lines(input)
        if self.showmap:
            self.output()

    def depth(self):
        return len(self.data)

    def width(self):
        return len(self.data[0])

    def get(self, x: int, y: int) -> str:
        return self.data[y][x - self.offset]

    def set(self, x: int, y: int, val: str):
        self.data[y][x - self.offset] = val

    def output(self):

        for i, y in enumerate(range(len(self.data))):
            print(
                f"{i:2} { ''.join( [self.data[y][x] for x in range(len(self.data[y]))]) }"
            )

    def update_rock_lines(self, input: list[list[Point]]) -> None:
        for line in input:
            for start, end in zip(line[:-1], line[1:]):
                if start.x == end.x:
                    for y in range(min(start.y, end.y), max(start.y, end.y) + 1):
                        self.set(start.x, y, "#")
                elif start.y == end.y:
                    for x in range(min(start.x, end.x), max(start.x, end.x) + 1):
                        self.set(x, start.y, "#")
                else:
                    raise Exception("Diagonal line!!")

        for x in range(0, self.width()):
            self.set(x + self.offset, self.depth() - 1, "#")

    def sandfall(self, startx: int, stop_at_bottom: bool = True) -> int:
        sand_blocks = 0
        while True:
            x = startx
            y = 0
            while True:
                if stop_at_bottom and y == self.depth() - 2:
                    if self.showmap:
                        self.output()
                    return sand_blocks
                elif self.get(x, y + 1) == ".":
                    y += 1
                    continue
                elif self.get(x - 1, y + 1) == ".":
                    y += 1
                    x -= 1
                    continue
                elif self.get(x + 1, y + 1) == ".":
                    y += 1
                    x += 1
                    continue
                elif y == 0:
                    self.set(x, y, "o")
                    if self.showmap:
                        self.output()
                    return sand_blocks + 1
                else:
                    break

            self.set(x, y, "o")
            sand_blocks += 1


class RockParser(au.Parser):
    def parse(self, line: str, strip: bool = True) -> list[Point]:

        return [
            Point(*[int(p) for p in spoint.split(",")]) for spoint in line.split(" -> ")
        ]


def test_one(input: list[list[Point]]) -> Optional[int]:

    return Map(input).sandfall(500)


def part_one(input: list[list[Point]]) -> Optional[int]:

    return Map(input).sandfall(500)


def test_two(input: list[list[Point]]) -> Optional[int]:
    return Map(input).sandfall(500, stop_at_bottom=False)


def part_two(input: list[list[Point]]) -> Optional[int]:
    return Map(input).sandfall(500, stop_at_bottom=False)


if __name__ == "__main__":
    day = au.Day(
        2022,
        14,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=RockParser(),
        input=RockParser(),
    )

    day.run_all(run_tests=True)
