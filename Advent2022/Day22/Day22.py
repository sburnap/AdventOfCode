from typing import Optional, Generator
from dataclasses import dataclass
import aoc_utils as au


@dataclass
class Turtle:
    x: int
    y: int
    facing: int
    maxx: int
    maxy: int

    def location(self) -> tuple[int, int]:
        return self.x, self.y

    def next(self, current: tuple[int, int]) -> tuple[int, int]:
        x, y = current
        match self.facing:
            case 0:
                return x + 1 if x < self.maxx - 1 else 0, y
            case 1:
                return (
                    x,
                    y + 1 if y < self.maxy - 1 else 0,
                )
            case 2:
                return x - 1 if x > 0 else self.maxx - 1, y
            case 3:
                return x, y - 1 if y > 0 else self.maxy
            case _:
                raise Exception(f"Bad facing {self.facing}")

    def moveto(self, target: tuple[int, int]):
        self.x = target[0]
        self.y = target[1]


@dataclass
class Map:
    data: list[str]

    def get(self, pos: tuple[int, int]) -> str:
        x, y = pos
        if y >= len(self.data):
            return " "
        if x >= len(self.data[y]):
            return " "
        return self.data[y][x]


def command_gen(commandlist: str) -> Generator[int | str, None, None]:
    current = ""
    for ch in commandlist:
        match ch:
            case "R" | "L":
                yield int(current)
                current = ""
                yield ch
            case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0":
                current += ch
            case _:
                raise Exception(f"Bad value {ch} in command")

    yield int(current)


def walk_around(input: list[str | list[str | int]]) -> Optional[int]:
    map = Map([l[0] for l in input[:-1] if type(l[0]) is str])
    commands = input[-1]

    turtle = Turtle(
        x=0,
        y=0,
        facing=0,
        maxx=max(len(map.data[y]) for y in range(len(map.data))),
        maxy=len(map.data),
    )
    for command in commands:
        match command:
            case "R":
                turtle.facing = (turtle.facing + 1) % 4
            case "L":
                turtle.facing = (turtle.facing - 1) % 4
            case int():
                for _ in range(command):
                    next = turtle.next(turtle.location())
                    working = True
                    while working:
                        if map.get(next) == ".":
                            turtle.moveto(next)
                            break
                        elif map.get(next) == " ":
                            next = turtle.next(next)
                        else:
                            working = False
                    if not working:
                        break

    row = turtle.y + 1
    column = turtle.x + 1
    return row * 1000 + column * 4 + turtle.facing


def test_one(input: list[str | list[str | int]]) -> Optional[int]:
    return walk_around(input)


def part_one(input: list[str | list[str | int]]) -> Optional[int]:
    return walk_around(input)


def test_two(input: str) -> Optional[int]:
    return None


def part_two(input: list[str]) -> Optional[int]:
    return None


if __name__ == "__main__":

    monkey_map_parser = au.RegexParser(
        [
            (r"^$", lambda m: None),
            (r"^([ \.#]*)$", lambda m: m),
            (r"^(([\d]*|L|R)*)$", lambda m: [cmd for cmd in command_gen(m[0])]),
        ]
    )
    day = au.Day(
        2022,
        22,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=monkey_map_parser,
        input=monkey_map_parser,
    )

    day.run_all(run_tests=True)
