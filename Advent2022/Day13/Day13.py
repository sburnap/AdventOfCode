from typing import Optional, Any
from functools import cmp_to_key
import json

import aoc_utils as au

Packet = int | list["Packet"]


def compare(first: Packet, second: Packet) -> int:

    assert type(first) == list
    assert type(second) == list

    for a, b in zip(first, second):
        if type(a) == int and type(b) == int:
            if a < b:
                return 1
            elif a > b:
                return -1
        else:
            if type(a) == int:
                a = [a]
            if type(b) == int:
                b = [b]

            if (result := compare(a, b)) != 0:
                return result

    if len(first) < len(second):
        return 1
    elif len(first) > len(second):
        return -1

    return 0


def test_one(packets: list[Packet | str]) -> Optional[int]:

    return sum(
        i + 1
        for i, pair in enumerate(zip(packets[::3], packets[1::3]))
        if compare(*pair) > 0
    )


def part_one(packets: list[Packet | str]) -> Optional[int]:
    l1 = [
        i + 1
        for i, pair in enumerate(zip(packets[::3], packets[1::3]))
        if compare(*pair) > 0
    ]
    return sum(l1)


def test_two(packets: list[Packet | str]) -> Optional[int]:
    ordered = sorted(
        [packet for packet in packets if type(packet) is Packet] + [[[2]], [[6]]],
        key=cmp_to_key(compare),
        reverse=True,
    )
    return (ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1)


def part_two(packets: list[Packet | str]) -> Optional[int]:
    ordered = sorted(
        [packet for packet in packets if type(packet) is not str] + [[[2]], [[6]]],
        key=cmp_to_key(compare),
        reverse=True,
    )
    return (ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1)


if __name__ == "__main__":
    signal_parser = au.RegexParser(
        [(r"^(\[.*\])$", lambda m: json.loads(m[0])), (r"^$", lambda m: "")]
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
