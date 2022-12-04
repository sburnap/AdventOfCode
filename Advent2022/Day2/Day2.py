import aoc_utils as au


def score(them: str, me: str):
    return [[4, 8, 3], [1, 5, 9], [7, 2, 6]][ord(them) - ord("A")][ord(me) - ord("X")]


# expected 15
def test_one(input: list[str]) -> int:
    return sum([score(*game.split()) for game in input])


# expected 10404
def part_one(input: list[str]) -> int:
    return sum([score(*game.split()) for game in input])


def score2(them: str, me: str):
    return [[3, 4, 8], [1, 5, 9], [2, 6, 7]][ord(them) - ord("A")][ord(me) - ord("X")]


# expected 12
def test_two(input: list[str]) -> int:
    return sum([score2(*game.split()) for game in input])


# expected 10334
def part_two(input: list[str]) -> int:
    return sum([score2(*game.split()) for game in input])


if __name__ == "__main__":
    day = au.Day(2022, 2, test_one, test_two, part_one, part_two)

    day.run_all(run_tests=True)
