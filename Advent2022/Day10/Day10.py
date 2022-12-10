from typing import Optional, Generator
from dataclasses import dataclass

import aoc_utils as au


@dataclass
class Noop:
    pass


@dataclass
class Add:
    value: int


def machine(opcodes: list[Noop | Add]) -> Generator[int, None, None]:
    X = 1
    clock = 1

    for opcode in opcodes:
        clock += 1
        if clock % 40 == 20:
            yield X * clock
        if type(opcode) == Add:
            X += opcode.value
            clock += 1
            if clock % 40 == 20:
                yield X * clock


def test_one(opcodes: list[Noop | Add]) -> Optional[int]:

    return sum(machine(opcodes))


def part_one(opcodes: list[Noop | Add]) -> Optional[int]:
    return sum(machine(opcodes))


def crt(opcodes: list[Noop | Add]) -> Generator[str, None, None]:
    X = 1
    clock = 0
    for opcode in opcodes:
        for _ in range(1 if type(opcode) == Noop else 2):
            yield "#" if abs(X - clock % 40) <= 1 else "."
            clock += 1
            if clock % 40 == 0:
                yield "\n"

        if type(opcode) == Add:
            X += opcode.value


def test_two(opcodes: list[Noop | Add]) -> Optional[int]:
    print(f'\n{"".join([ch for ch in crt(opcodes)])}')
    return None


def part_two(opcodes: list[Noop | Add]) -> Optional[int]:
    print(f'\n{"".join([ch for ch in crt(opcodes)])}')
    return None


if __name__ == "__main__":
    opcode_parser = au.RegexParser(
        [(r"^noop$", lambda m: Noop()), (r"addx (-?\d*)$", lambda m: Add(int(m[0])))]
    )
    day = au.Day(
        2022,
        10,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=opcode_parser,
        input=opcode_parser,
    )

    day.run_all(run_tests=True)
