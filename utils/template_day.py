from functools import reduce
import operator

import aoc_utils as au


def test_one(day: au.Day, test_input: str) -> int:
    return "I dunno"


def part_one(day: au.Day, input: list[str]) -> int:
    return "I dunno"


def test_two(day: au.Day, test_input: str) -> int:
    return "I dunno"


def part_two(day: au.Day, input: list[str]) -> int:
    return "I dunno"


if __name__ == "__main__":
    day = au.Day(
        2015,
        3,
        test_one,
        test_two,
        part_one,
        part_two,
        input=au.Day.InType.INPUT_MULTI_LINE_STR,
        test_input=None,
    )

    day.run_all(run_tests=True)
