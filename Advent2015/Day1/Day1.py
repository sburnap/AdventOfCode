from typing import Optional

import aoc_utils as au


def calculate_floor(input: str) -> tuple[int, Optional[int]]:
    floor = 0
    basement = None

    for step, ch in enumerate(input):
        match ch:

            case "(":
                floor += 1
            case ")":
                floor -= 1
            case _:
                raise Exception(
                    f"Bad character '{ch}' found in position {step} for input {input[:10]}"
                )
        if floor < 0 and basement == None:
            basement = step + 1

    return floor, basement


def test_one(test_input):
    return calculate_floor(test_input)[0]


def part_one(input):
    return calculate_floor(input)[0]


def test_two(test_input):
    return calculate_floor(test_input)[1]


def part_two(input):
    return calculate_floor(input)[1]


if __name__ == "__main__":
    day = au.Day(
        2015,
        1,
        test_one,
        test_two,
        part_one,
        part_two,
        input=au.Day.InType.INPUT_ONE_LINE_STR,
        test_input=["(())", "()()", "(((", "(()(()(", "())", ")())())", ")", "()())"],
    )

    day.run_all(run_tests=True)
