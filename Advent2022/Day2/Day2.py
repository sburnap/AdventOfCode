import aoc_utils as au


def score(them: str, me: str):

    return (
        "?XYZ".index(me)
        + {"A": [3, 6, 0], "B": [0, 3, 6], "C": [6, 0, 3]}[them][ord(me) - ord("X")]
    )


# expected 15
def test_one(input: list[tuple[str, str]]) -> int:
    return sum([score(*game) for game in input])


# expected 10404
def part_one(input: list[tuple[str, str]]) -> int:
    return sum([score(*game) for game in input])


def move(them: str, me: str):

    return {
        "A": {"X": "Z", "Y": "X", "Z": "Y"},
        "B": {"X": "X", "Y": "Y", "Z": "Z"},
        "C": {"X": "Y", "Y": "Z", "Z": "X"},
    }[them][me]


# expected 12
def test_two(input: list[tuple[str, str]]) -> int:
    return sum([score(game[0], move(*game)) for game in input])


# expected 10334
def part_two(input: list[tuple[str, str]]) -> int:
    return sum([score(game[0], move(*game)) for game in input])


if __name__ == "__main__":
    game_parser = au.RegexParser([(r"(.) (.)", lambda m: (m[0], m[1]))])

    day = au.Day(
        2022,
        2,
        test_one,
        test_two,
        part_one,
        part_two,
        input=game_parser,
        test_input=game_parser,
    )

    day.run_all(run_tests=True)
