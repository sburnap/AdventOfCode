from typing import Generator

import aoc_utils as au


def read_elves(foods: list[str]) -> Generator[int, None, None]:

    calories = 0
    for food in foods:
        if food == "":
            yield calories
            calories = 0
        else:
            calories += int(food)


# expected 24000
def test_one(foods: list[str]) -> int:
    return max(read_elves(foods))


# expected 67016
def part_one(foods: list[str]) -> int:
    return max(read_elves(foods))


# expected 45000
def test_two(foods: list[str]) -> int:
    return sum(sorted(read_elves(foods))[-3:])


# expected 200116
def part_two(foods: list[str]) -> int:
    return sum(sorted(read_elves(foods))[-3:])


if __name__ == "__main__":
    day = au.Day(
        2022,
        1,
        test_one,
        test_two,
        part_one,
        part_two,
        input=au.Day.InType.INPUT_MULTI_LINE_STR,
        test_input=au.Day.InType.INPUT_MULTI_LINE_STR,
    )

    day.run_all(run_tests=True)
