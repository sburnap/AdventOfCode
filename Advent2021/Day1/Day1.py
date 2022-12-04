import aoc_utils as au


def number_increasing(input):
    return len([i for i in [a < b for a, b in zip(input, input[1:])] if i == True])


def test_one(input: str) -> int:
    return number_increasing(input)


# expected 1184
def part_one(input: list[str]) -> int:
    return number_increasing(input)


def in_threes(input):
    return [sum(x) for x in zip(input, input[1:], input[2:])]


def test_two(input: str) -> int:
    return number_increasing(in_threes(input))


# expected 1158
def part_two(input: list[str]) -> int:
    return number_increasing(in_threes(input))


if __name__ == "__main__":
    day = au.Day(
        2021,
        1,
        test_one,
        test_two,
        part_one,
        part_two,
        input=au.IntParser(),
        test_input=au.IntParser(),
    )

    day.run_all(run_tests=True)
