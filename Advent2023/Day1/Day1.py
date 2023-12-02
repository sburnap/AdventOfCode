from typing import Optional

import aoc_utils as au

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def first_digit(s: str, use_english: bool) -> str:
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i]
        elif use_english:
            for name in digits:
                if s[i:].startswith(name):
                    return str(digits[name])

    return None


def last_digit(s: str, use_english: bool) -> str:
    for i in range(len(s) - 1, -1, -1):
        if s[i].isdigit():
            return s[i]
        elif use_english:
            for name in digits:
                if s[i:].startswith(name):
                    return str(digits[name])

    return None


def test_one(lines: list[str]) -> Optional[int]:
    return sum(
        int(first_digit(line, use_english=False) + last_digit(line, use_english=False))
        for line in lines
    )


def part_one(lines: list[str]) -> Optional[int]:
    return sum(
        int(first_digit(line, use_english=False) + last_digit(line, use_english=False))
        for line in lines
    )


def test_two(lines: list[str]) -> Optional[int]:
    return sum(
        int(first_digit(line, use_english=True) + last_digit(line, use_english=True))
        for line in lines
    )


def part_two(lines: list[str]) -> Optional[int]:
    return sum(
        int(first_digit(line, use_english=True) + last_digit(line, use_english=True))
        for line in lines
    )


if __name__ == "__main__":
    day = au.Day(2023, 1, test_one, test_two, part_one, part_two)

    day.run_all(run_tests=True)
