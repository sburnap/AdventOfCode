import aoc_utils as au


def expand(input: str) -> str:

    current = None
    cnt = 0
    rc = ""
    for ch in input:
        if current == ch:
            cnt += 1
            continue
        elif current:
            rc += f"{cnt}{current}"

        cnt = 1
        current = ch

    rc += f"{cnt}{current}"

    return rc


def test_one(input: str) -> str:
    return expand(input)


def part_one(input: str) -> int:
    current = input
    for i in range(40):
        current = expand(current)

    return len(current)


def test_two(input: str) -> str:
    return expand(input)


def part_two(input: str) -> int:
    current = input
    for i in range(50):
        current = expand(current)

    return len(current)


if __name__ == "__main__":
    day = au.Day(
        2015,
        10,
        test_one,
        test_two,
        part_one,
        part_two,
        input="1113122113",
        test_input=["1", "11", "21", "1211", "111221"],
    )

    day.run_all(run_tests=True)
