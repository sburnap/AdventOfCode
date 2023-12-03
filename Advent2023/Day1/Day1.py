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


def eval_as_digit(s: str, use_english: bool) -> Optional[str]:
    if s[0].isdigit():
        return s[0]
    elif use_english:
        for name in digits:
            if s.startswith(name):
                return str(digits[name])
    return None


def first_digit(s: str, use_english: bool = False) -> str:
    for i in range(len(s)):
        if (digit := eval_as_digit(s[i:], use_english)) is not None:
            return digit


def last_digit(s: str, use_english: bool = False) -> str:
    for i in range(len(s) - 1, -1, -1):
        if (digit := eval_as_digit(s[i:], use_english)) is not None:
            return digit


# expect 142
def test_one(lines: list[str]) -> Optional[int]:
    return sum(int(first_digit(line) + last_digit(line)) for line in lines)


# expect 54573
def part_one(lines: list[str]) -> Optional[int]:
    return sum(int(first_digit(line) + last_digit(line)) for line in lines)


# expect 281
def test_two(lines: list[str]) -> Optional[int]:
    return sum(
        int(first_digit(line, use_english=True) + last_digit(line, use_english=True))
        for line in lines
    )


# expect 54591
def part_two(lines: list[str]) -> Optional[int]:
    return sum(
        int(first_digit(line, use_english=True) + last_digit(line, use_english=True))
        for line in lines
    )


if __name__ == "__main__":
    day = au.Day(2023, 1, test_one, test_two, part_one, part_two)

    day.run_all(run_tests=True)
