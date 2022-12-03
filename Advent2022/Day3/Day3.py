from typing import Generator

import aoc_utils as au


def inboth(rucksack: str) -> str:
    return (
        set(rucksack[: len(rucksack) // 2]) & set(rucksack[len(rucksack) // 2 :])
    ).pop()


def score(char: str) -> int:
    return 1 + (ord(char) - ord("a") if char.islower() else 26 + ord(char) - ord("A"))


# expected 157
def test_one(input: list[str]) -> int:
    return sum([score(inboth(rucksack)) for rucksack in input])


# expected 7845
def part_one(input: list[str]) -> int:
    return sum([score(inboth(rucksack)) for rucksack in input])


def in_three(first: str, second: str, third: str) -> str:
    return (set(first) & set(second) & set(third)).pop()


# expected 70
def test_two(input: list[str]) -> int:
    return sum(
        score(in_three(*triplet))
        for triplet in zip(input[0::3], input[1::3], input[2::3])
    )


# expected 2790
def part_two(input: list[str]) -> int:
    return sum(
        score(in_three(*triplet))
        for triplet in zip(input[0::3], input[1::3], input[2::3])
    )


if __name__ == "__main__":
    day = au.Day(
        2022,
        3,
        test_one,
        test_two,
        part_one,
        part_two,
        input=au.Day.InType.INPUT_MULTI_LINE_STR,
        test_input=au.Day.InType.INPUT_MULTI_LINE_STR,
    )

    day.run_all(run_tests=True)
