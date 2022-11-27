import aoc_utils as au


def travel(input):
    height = 0
    depth = 0
    for command, amount in input:
        if command == "forward":
            height += amount
        elif command == "down":
            depth += amount
        elif command == "up":
            depth -= amount

    return height, depth


def test_one(input: str) -> int:
    height, depth = travel(input)
    return height * depth


# expected 1855814
def part_one(input: list[str]) -> int:
    height, depth = travel(input)
    return height * depth


def travel2(input):
    height = 0
    deptheight = 0
    aim = 0
    for command, amount in input:
        if command == "forward":
            height += amount
            deptheight += amount * aim
        elif command == "down":
            aim += amount
        elif command == "up":
            aim -= amount

    return height, deptheight


def test_two(input: str) -> int:
    height, depth = travel2(input)
    return height * depth


# expected 1845455714
def part_two(input: list[str]) -> int:
    height, depth = travel2(input)
    return height * depth


if __name__ == "__main__":
    command_parser = au.RegexParser(
        [("(forward|down|up) (.*)", lambda x: (x[0], int(x[1])))]
    )

    day = au.Day(
        2021,
        2,
        test_one,
        test_two,
        part_one,
        part_two,
        input=command_parser,
        test_input=command_parser,
    )

    day.run_all(run_tests=True)
