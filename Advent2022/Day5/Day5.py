from typing import Optional
from dataclasses import dataclass

import aoc_utils as au


@dataclass
class Order:
    number: int
    source: int
    target: int


def get_stacks(crates: list[str]) -> list[list[str]]:
    num_stacks = int(crates[-1].split()[-1])
    stacks: list[list[str]] = [[] for _ in range(num_stacks)]

    for crate_line in crates[:-1]:
        crates = [crate_line[i] for i in range(1, len(crate_line), 4)]
        for i in range(1, len(crate_line), 4):
            if crate_line[i] != " ":
                stacks[(i - 1) // 4].append(crate_line[i])
    return stacks


def do_orders(stacks: list[list[str]], orders: list[Order], reverse: bool) -> str:
    for order in orders:
        to_move = stacks[order.source][: order.number]
        if reverse:
            to_move = to_move[::-1]

        stacks[order.target] = to_move + stacks[order.target]
        stacks[order.source] = stacks[order.source][order.number :]

    return "".join([stack[0] for stack in stacks])


def test_one(input: list[Order | str]) -> Optional[str]:

    return do_orders(
        stacks=get_stacks([item for item in input if type(item) == str and item != ""]),
        orders=[item for item in input if type(item) == Order],
        reverse=True,
    )


def part_one(input: list[Order | str]) -> Optional[str]:
    return do_orders(
        stacks=get_stacks([item for item in input if type(item) == str and item != ""]),
        orders=[item for item in input if type(item) == Order],
        reverse=True,
    )


def test_two(input: list[Order | str]) -> Optional[str]:
    return do_orders(
        stacks=get_stacks([item for item in input if type(item) == str and item != ""]),
        orders=[item for item in input if type(item) == Order],
        reverse=False,
    )


def part_two(input: list[Order | str]) -> Optional[str]:
    return do_orders(
        stacks=get_stacks([item for item in input if type(item) == str and item != ""]),
        orders=[item for item in input if type(item) == Order],
        reverse=False,
    )


if __name__ == "__main__":
    crate_parser = au.RegexParser(
        [
            (
                r"move (\d*) from (\d*) to (\d*)",
                lambda m: Order(int(m[0]), int(m[1]) - 1, int(m[2]) - 1),
            ),
            (r"(.*)", lambda m: m[0]),
        ]
    )
    day = au.Day(2022, 5, test_one, test_two, part_one, part_two, input=crate_parser)

    day.run_all(run_tests=True)
