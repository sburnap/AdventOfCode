from typing import Optional

import aoc_utils as au


def test_one(day: au.Day, test_input):
    return "I dunno"


def part_one(day: au.Day):
    return "I dunno"


def test_two(day: au.Day, test_input):
    return "I dunno"


def part_two(day: au.Day):
    return "I dunno"


if __name__ == "__main__":
    day = au.Day(
        2015, 1, test_one, test_two, part_one, part_two, input=None, test_input=None
    )

    day.run_all(run_tests=True)
