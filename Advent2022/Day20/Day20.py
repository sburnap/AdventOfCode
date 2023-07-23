from typing import Optional
from collections import Counter

import aoc_utils as au


def decrypt(input: list[int]) -> int:
    ring = [item for item in input]
    length = len(ring)
    locations = list(range(length))

    # print(f"{ring} ")
    for i in range(length):
        loc = locations[i]
        num = ring[loc]

        assert num == input[i]

        if num == 0:
            continue

        if num > 0:
            target = loc + num
        else:
            target = (loc + num) - 1

        while target < 1:
            target += length
        while target >= length:
            target -= length

        assert target > 0
        assert target <= length

        if loc > target:
            ring = ring[: target + 1] + [num] + ring[target + 1 : loc] + ring[loc + 1 :]
            locations = (
                locations[: target + 1]
                + [i]
                + locations[target + 1 : loc]
                + locations[loc + 1 :]
            )

        else:
            ring = ring[:loc] + ring[loc + 1 : target + 1] + [num] + ring[target + 1 :]
            locations = (
                locations[:loc]
                + locations[loc + 1 : target + 1]
                + [i]
                + locations[target + 1 :]
            )

        print(f"{ring} -> {num}")

    loc = ring.index(0)
    assert loc >= 0
    return (
        ring[(loc + 1000) % length]
        + ring[(loc + 2000) % length]
        + ring[(loc + 3000) % length]
    )


def test_one(input: list[int]) -> Optional[int]:
    return decrypt(input)


def part_one(input: list[int]) -> Optional[int]:
    return None
    return decrypt(input)


def test_two(input: list[int]) -> Optional[int]:
    return None


def part_two(input: list[int]) -> Optional[int]:
    return None


if __name__ == "__main__":
    day = au.Day(
        2022,
        20,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=au.IntParser(),
        input=au.IntParser(),
    )

    day.run_all(run_tests=True)
