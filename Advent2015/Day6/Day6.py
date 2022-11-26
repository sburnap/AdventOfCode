import re
from dataclasses import dataclass
from typing import Callable, Optional, Generator, Any

import aoc_utils as au


@dataclass
class Rect:
    x1: int
    y1: int
    x2: int
    y2: int


PerformFunc = Callable[[list[list[int]], int, int, str], None]


def perform_part_one(lights: list[list[int]], x: int, y: int, instruction: str) -> None:
    match instruction:
        case "turn on":
            lights[x][y] = 1
        case "turn off":
            lights[x][y] = 0
        case "toggle":
            lights[x][y] = 1 if lights[x][y] == 0 else 0


def brute(commands: list[Optional[tuple[str, Rect]]], fn):
    lights = [[0] * 1000 for _ in range(1000)]

    for command in filter(None, commands):
        for x in range(command[1].x1, command[1].x2 + 1):
            for y in range(command[1].y1, command[1].y2 + 1):
                fn(lights, x, y, command[0])

    return sum([sum([light for light in line]) for line in lights])


def test_one(input: list[str]) -> int:
    return brute(input, perform_part_one)


def part_one(input: list[str]) -> int:
    return brute(input, perform_part_one)


def perform_part_two(lights: list[list[int]], x: int, y: int, instruction: str) -> None:
    match instruction:
        case "turn on":
            lights[x][y] += 1
        case "turn off":
            if lights[x][y] > 0:
                lights[x][y] -= 1
        case "toggle":
            lights[x][y] += 2


def test_two(input: list[str]) -> int:
    return brute(input, perform_part_two)


def part_two(input: list[str]) -> int:
    return brute(input, perform_part_two)


if __name__ == "__main__":
    command_parser = au.RegexParser(
        ["(.*) (\d*),(\d*) through (\d*),(\d*)"],
        lambda x: (str(x[0]), Rect(int(x[1]), int(x[2]), int(x[3]), int(x[4]))),
    )

    day = au.Day(
        2015,
        6,
        test_one,
        test_two,
        part_one,
        part_two,
        input=command_parser,
        test_input=command_parser,
    )

    day.run_all(run_tests=True)
