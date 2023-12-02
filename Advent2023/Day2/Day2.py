from typing import Optional

import aoc_utils as au

def test_one(input: str) -> Optional[int]:
    return None


def part_one(input: list[str]) -> Optional[int]:
    return None


def test_two(input: str) -> Optional[int]:
    return None


def part_two(input: list[str]) -> Optional[int]:
    return None

if __name__ == "__main__":
    day = au.Day(
        2023,
        2,
        test_one,
        test_two,
        part_one,
        part_two
    )

    day.run_all(run_tests=True)
