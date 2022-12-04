from itertools import combinations
import aoc_utils as au


def number_combos(input: list[int], amount: int) -> int:
    return sum(
        [
            len([l for l in combinations(input, i) if sum(l) == amount])
            for i in range(1, len(input))
        ]
    )


def test_one(input: list[int]) -> int:
    return number_combos(input, 25)


# expect 1638
def part_one(input: list[int]) -> int:
    return number_combos(input, 150)


def number_fixed_combos(input: list[int], amount: int, combos: int) -> int:
    return len([l for l in combinations(input, combos) if sum(l) == amount])


def number_min_combos(input: list[int], amount: int) -> int:
    for i in range(1, len(input)):
        if (combos := number_fixed_combos(input, amount, i)) != 0:
            return combos

    return 0


def test_two(input: list[int]) -> int:
    return number_min_combos(input, 25)


# expect 17
def part_two(input: list[int]) -> int:
    return number_min_combos(input, 150)


if __name__ == "__main__":
    day = au.Day(
        2015,
        17,
        test_one,
        test_two,
        part_one,
        part_two,
        input=au.IntParser(),
        test_input=au.IntParser(),
    )

    day.run_all(run_tests=True)
