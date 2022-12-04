from typing import Any
from dataclasses import dataclass
from itertools import permutations

import aoc_utils as au


def score(table: tuple[str, ...], rules):
    sm = 0
    for i, person in enumerate(table):
        left = i - 1 if i > 0 else len(table) - 1
        right = i + 1 if i < len(table) - 1 else 0

        sm += rules[person][table[left]] + rules[person][table[right]]
    return sm


def build_scores(input: list[tuple[str, str, int]]) -> dict[str, dict[str, int]]:
    scores: dict[str, dict[str, int]] = {}

    for person, next_to, gain in input:
        scores.setdefault(person, {})[next_to] = gain

    return scores


def test_one(input: list[tuple[str, str, int]]) -> int:

    scores = build_scores(input)

    possibles = list(permutations(scores.keys()))
    return max([score(possible, scores) for possible in possibles])


def part_one(input: list[tuple[str, str, int]]) -> int:
    scores = build_scores(input)

    possibles = list(permutations(scores.keys()))
    return max([score(possible, scores) for possible in possibles])


def add_santa(scores: dict[str, dict[str, int]]) -> dict[str, dict[str, int]]:
    for person in list(scores.keys()):
        scores.setdefault("Santa", {})[person] = 0
        scores[person]["Santa"] = 0

    return scores


def part_two(input: list[tuple[str, str, int]]) -> int:
    scores = add_santa(build_scores(input))

    possibles = list(permutations(scores.keys()))
    return max([score(possible, scores) for possible in possibles])


if __name__ == "__main__":
    happy_parser = au.RegexParser(
        [
            (
                "(.*) would gain (\d*) happiness units by sitting next to (.*)\.",
                lambda m: (m[0], m[2], int(m[1])),
            ),
            (
                "(.*) would lose (\d*) happiness units by sitting next to (.*)\.",
                lambda m: (m[0], m[2], -int(m[1])),
            ),
        ]
    )

    day = au.Day(
        2015,
        13,
        test_one,
        None,
        part_one,
        part_two,
        input=happy_parser,
        test_input=happy_parser,
    )

    day.run_all(run_tests=True)
