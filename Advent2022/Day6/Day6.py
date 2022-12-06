from typing import Optional

import aoc_utils as au


def distinct_start(input: str, number: int) -> Optional[int]:
    for i in range(number, len(input)):
        if len(set(input[i - number : i])) == number:
            return i

    return None


def test_one(input: str) -> Optional[int]:
    return distinct_start(input, 4)


# expected 1155
def part_one(input: str) -> Optional[int]:
    return distinct_start(input, 4)


def test_two(input: str) -> Optional[int]:
    return distinct_start(input, 14)


# expected 2789
def part_two(input: str) -> Optional[int]:
    return distinct_start(input, 14)


if __name__ == "__main__":
    day = au.Day(
        2022,
        6,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=[
            "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
            "bvwbjplbgvbhsrlpgdmjqwftvncz",
            "nppdvjthqldpwncqszvftbrmjlhg",
            "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
            "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
        ],
        input=au.OneLineParser(),
    )

    day.run_all(run_tests=True)
