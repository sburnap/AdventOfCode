from typing import Optional
from functools import cmp_to_key
import json

import aoc_utils as au

Packet = int | list["Packet"]


def force_list(a: Packet) -> Packet:
    return [a] if type(a) is int else a


def compare(first: Packet, second: Packet) -> int:

    # asserts are the only way I can make mypy happy
    assert type(first) == list
    assert type(second) == list

    for a, b in zip(first, second):
        if type(a) == int and type(b) == int:
            if (diff := b - a) != 0:
                return diff
        elif (result := compare(force_list(a), force_list(b))) != 0:
            return result

    return len(second) - len(first)


def sum_right_order(packets: list[Packet]) -> Optional[int]:
    return sum(
        i + 1
        for i, pair in enumerate(zip(packets[::3], packets[1::3]))
        if compare(*pair) > 0
    )


def test_one(packets: list[Packet]) -> Optional[int]:
    return sum_right_order(packets)


def part_one(packets: list[Packet]) -> Optional[int]:
    return sum_right_order(packets)


def find_signal_spot(packets: list[Packet]) -> Optional[int]:
    ordered = sorted(
        [packet for packet in packets] + [[[2]], [[6]]],
        key=cmp_to_key(compare),
        reverse=True,
    )
    return (ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1)


def test_two(packets: list[Packet]) -> Optional[int]:
    return find_signal_spot(packets)


def part_two(packets: list[Packet]) -> Optional[int]:
    return find_signal_spot(packets)


if __name__ == "__main__":
    signal_parser = au.RegexParser(
        [(r"^(\[.*\])$", lambda m: json.loads(m[0])), (r"^$", lambda m: None)]
    )
    day = au.Day(
        2022,
        13,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=signal_parser,
        input=signal_parser,
    )

    day.run_all(run_tests=True)
