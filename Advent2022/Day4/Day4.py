import aoc_utils as au
from dataclasses import dataclass


@dataclass
class Area:
    start: int
    end: int


def contains(first: Area, second: Area) -> bool:
    return (first.start <= second.start and first.end >= second.end) or (
        second.start <= first.start and second.end >= first.end
    )


def test_one(input: list[tuple[Area, Area]]) -> int:
    return len([pair for pair in input if contains(*pair)])


def part_one(input: list[tuple[Area, Area]]) -> int:
    return len([pair for pair in input if contains(*pair)])


def overlap(first: Area, second: Area) -> bool:
    return (second.start <= first.start <= second.end) or (
        first.start <= second.start <= first.end
    )


def test_two(input: list[tuple[Area, Area]]) -> int:
    return len([pair for pair in input if overlap(*pair)])


def part_two(input: list[tuple[Area, Area]]) -> int:
    return len([pair for pair in input if overlap(*pair)])


if __name__ == "__main__":
    pair_parser = au.RegexParser(
        [
            (
                "(\d*)-(\d*),(\d*)-(\d*)",
                lambda m: (Area(int(m[0]), int(m[1])), Area(int(m[2]), int(m[3]))),
            )
        ]
    )
    day = au.Day(
        2022,
        4,
        test_one,
        test_two,
        part_one,
        part_two,
        input=pair_parser,
        test_input=pair_parser,
    )

    day.run_all(run_tests=True)
