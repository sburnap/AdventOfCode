from typing import Optional, Generator
from functools import reduce
import operator

import aoc_utils as au


def divisors_num(num: int) -> Generator[int, None, None]:

    while num > 1:
        for i in range(2, num + 1):
            while num % i == 0:
                yield i
                num //= i


def num_presents(house: int) -> int:

    presents = 0
    for i in range(1, house + 1):
        if house % i == 0:
            presents += i * 10

    return presents


def test_one(input: int) -> Optional[int]:
    mx = 0
    for i in range(1, 100):
        presents = num_presents(i + 1)
        if presents > mx:
            mx = presents
        divisors = list(divisors_num((presents - 1) // 10))
        print(
            i + 1, mx, presents, divisors, 10 + reduce(operator.mul, divisors, 1) * 10
        )
    return None


def part_one(input: int) -> Optional[int]:
    target = input // 10

    divisors = list(divisors_num(target - 1))
    p = num_presents(divisors[-1])
    return sum(divisors)


def test_two(input: str) -> Optional[int]:
    return None


def part_two(input: list[str]) -> Optional[int]:
    return None


if __name__ == "__main__":
    day = au.Day(
        2015, 20, test_one, test_two, part_one, part_two, test_input=120, input=36000000
    )

    day.run_all(run_tests=True)
