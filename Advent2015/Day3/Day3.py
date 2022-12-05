from collections import Counter

import aoc_utils as au


class Mover:
    def __init__(self):
        self.x, self.y = 0, 0

    def move(self, direction: str) -> None:
        match direction:
            case ">":
                self.x += 1
            case "<":
                self.x -= 1
            case "v":
                self.y += 1
            case "^":
                self.y -= 1
            case _:
                raise Exception(f"Bad direction {direction} seen")


def count_houses(directions: str, n: int) -> int:

    assert n > 0

    houses: Counter = Counter()

    movers = [Mover() for _ in range(n)]

    for mover in movers:
        houses[(mover.x, mover.y)] += 1

    for i, direction in enumerate(directions):
        mover = movers[i % n]
        mover.move(direction)
        houses[(mover.x, mover.y)] += 1

    return len(houses)


def test_one(test_input: str) -> int:
    return count_houses(test_input, 1)


def part_one(input: str) -> int:
    return count_houses(input[0], 1)


def test_two(test_input: str) -> int:
    return count_houses(test_input, 2)


def part_two(input: str) -> int:
    return count_houses(input[0], 2)


if __name__ == "__main__":
    day = au.Day(
        2015,
        3,
        test_one,
        test_two,
        part_one,
        part_two,
        input=au.Parser(),
        test_input=[">", "^>v<", "^v^v^v^v^v", "^v"],
    )

    day.run_all(run_tests=True)
