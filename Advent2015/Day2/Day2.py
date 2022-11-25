from functools import reduce
import operator

import aoc_utils as au


def get_sides(box_size: str) -> list[int]:
    return [int(dim) for dim in box_size.split("x")]


def calc_paper(box_size: str) -> int:
    height, width, length = get_sides(box_size)
    sides = (2 * width * length, 2 * width * height, 2 * height * length)

    return sum(sides) + min(sides) // 2


def test_one(test_input: str) -> int:
    return calc_paper(test_input)


def part_one(input: list[str]) -> int:
    return sum(calc_paper(paper_def) for paper_def in input)


def calc_ribbon(box_size: str) -> int:
    sides = sorted(get_sides(box_size))
    return 2 * sides[0] + 2 * sides[1] + reduce(operator.mul, sides, 1)


def test_two(test_input: str) -> int:
    return calc_ribbon(test_input)


def part_two(input: list[str]) -> int:
    return sum(calc_ribbon(paper_def) for paper_def in input)


if __name__ == "__main__":
    day = au.Day(
        2015,
        2,
        test_one,
        test_two,
        part_one,
        part_two,
        input=au.Day.InType.INPUT_MULTI_LINE_STR,
        test_input=["2x3x4", "1x1x10"],
    )

    day.run_all(run_tests=True)
