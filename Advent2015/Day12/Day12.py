from typing import Generator, Any
import json

import aoc_utils as au


def get_numbers(input: str) -> Generator[int, None, None]:

    current = ""

    for ch in input:
        if ch.isdigit() or ch == "-":
            current += ch
        elif current != "":
            yield int(current)
            current = ""


def test_one(input: str) -> int:
    return sum([num for num in get_numbers(input)])


def part_one(input: list[str]) -> int:
    return sum([sum([num for num in get_numbers(line)]) for line in input])


def evaluate(js: dict[str, Any] | list[Any]) -> int:
    match js:
        case dict():
            if "red" in js.keys() or "red" in js.values():
                return 0
            else:
                return sum([evaluate(val) for val in js.values()])
        case int():
            return js
        case list():
            return sum([evaluate(val) for val in js])
        case str():
            return 0
        case _:
            raise Exception("Unknown type in json")


def test_two(input: str) -> int:
    return evaluate(json.loads(input))


def part_two(input: list[str]) -> int:
    return sum([evaluate(json.loads(line)) for line in input])


if __name__ == "__main__":
    day = au.Day(
        2015,
        12,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=[
            "[1,2,3]",
            '{"a":2,"b":4}',
            "[[[3]]]",
            '{"a":{"b":4},"c":-1}',
            '{"a":[-1,1]}',
            '[-1,{"a":1}]',
            "[]",
            "{}",
            '[1,{"c":"red","b":2},3]',
            '{"d":"red","e":[1,2,3,4],"f":5}',
            '[1,"red",5]',
        ],
    )

    day.run_all(run_tests=True)
