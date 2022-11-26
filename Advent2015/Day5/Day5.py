import aoc_utils as au


def is_nice(input: str) -> int:

    for bad in ["ab", "cd", "pq", "xy"]:
        if bad in input:
            return False

    if len([ch for ch in input if ch in "aeiou"]) < 3:
        return False

    for i in range(len(input) - 1):
        if input[i] == input[i + 1]:
            return True

    return False


def test_one(test_input: str) -> str:
    return "Nice!" if is_nice(test_input) else "Naughty!"


def part_one(input: list[str]) -> int:
    return len([string for string in input if is_nice(string)])


def is_nice2(input: str) -> int:
    test1 = False
    test2 = False
    for i in range(len(input) - 2):
        if input[i : i + 2] in input[i + 2 :]:
            test1 = True
        if input[i] == input[i + 2]:
            test2 = True

        if test1 and test2:
            return True

    return False


def test_two(test_input: str) -> str:
    return "Nice!" if is_nice2(test_input) else "Naughty!"


def part_two(input: list[str]) -> int:
    return len([string for string in input if is_nice2(string)])


if __name__ == "__main__":
    day = au.Day(
        2015,
        5,
        test_one,
        test_two,
        part_one,
        part_two,
        input=au.Day.InType.INPUT_MULTI_LINE_STR,
        test_input=[
            "ugknbfddgicrmopn",
            "aaa",
            "jchzalrnumimnmhp",
            "haegwjzuvuyypxyu",
            "dvszwmarrgswjxmb",
            "qjhvhtzxzqqjkmpb",
            "xxyxx",
            "uurcxstgmygtbstg",
            "ieodomkazucvgmuy",
        ],
    )

    day.run_all(run_tests=True)
