from typing import Optional
import re

import aoc_utils as au


def check_round(round: str) -> bool:
    blue = 0
    green = 0
    red = 0
    for color in round.split(","):
        match color.split():
            case [c, "blue"]:
                blue += int(c)
            case [c, "green"]:
                green += int(c)
            case [c, "red"]:
                red += int(c)
            case _:
                print("oh no")

    return red <= 12 and green <= 13 and blue <= 14


def calculate_power(game: str) -> int:
    re_blue = re.compile(r"(\d*) blue")
    re_green = re.compile(r"(\d*) green")
    re_red = re.compile(r"(\d*) red")

    return (
        max(int(c) for c in re_blue.findall(game[1]))
        * max(int(c) for c in re_green.findall(game[1]))
        * max(int(c) for c in re_red.findall(game[1]))
    )


# expect 8
def test_one(games: list[tuple[str, str]]) -> Optional[int]:
    return sum(
        int(game[0])
        for game in games
        if all(check_round(round) for round in game[1].split(";"))
    )


# expect 2512
def part_one(games: list[tuple[str, str]]) -> Optional[int]:
    return sum(
        int(game[0])
        for game in games
        if all(check_round(round) for round in game[1].split(";"))
    )


# expect 2286
def test_two(games: list[tuple[str, str]]) -> Optional[int]:
    return sum(calculate_power(game) for game in games)


# expect 67335
def part_two(games: list[tuple[str, str]]) -> Optional[int]:
    return sum(calculate_power(game) for game in games)


if __name__ == "__main__":
    game_parser = au.RegexParser([(r"^Game (\d*):(.*)$", lambda m: (m[0], m[1]))])
    day = au.Day(
        2023,
        2,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=game_parser,
        input=game_parser,
    )

    day.run_all(run_tests=True)
