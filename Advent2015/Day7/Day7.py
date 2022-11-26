from typing import Optional
import re
from functools import cache

import aoc_utils as au


class Command:
    def __init__(
        self, name: str, operand1: str | int, operand2: str | int | None, target: str
    ):
        self.name = name
        self.operand1: str | int
        self.operand2: str | int | None
        try:
            self.operand1 = int(operand1)
        except ValueError:
            self.operand1 = operand1
        try:
            self.operand2 = int(operand2) if operand2 else operand2
        except (ValueError):
            self.operand2 = operand2
        self.target = target


class Machine:
    def __init__(self, command_list: list[Command]):
        self.machine = {command.target: command for command in command_list}

    @cache
    def evaluate(self, wire: str) -> int:
        command: Command = self.machine[wire]

        if type(command.operand1) == int:
            op1 = command.operand1
        elif command.operand1:
            op1 = self.evaluate(command.operand1)

        if type(command.operand2) == int:
            op2 = command.operand2
        elif command.operand2:
            op2 = self.evaluate(command.operand2)

        match command.name:
            case "ASSIGN":
                return op1
            case "NOT":
                return ~op1 & 0xFFFF
            case "AND":
                return op1 & op2
            case "OR":
                return op1 | op2
            case "LSHIFT":
                return op1 << op2
            case "RSHIFT":
                return op1 >> op2
            case _:
                raise Exception(f"Bad command {command.name}")


def parse_command(command: str) -> Command:
    assign_re = re.compile("([^\s]*) -> ([^\s]*)")
    not_re = re.compile("NOT ([^\s]*) -> ([^\s]*)")
    other_re = re.compile("([^\s]*) (AND|OR|LSHIFT|RSHIFT) ([^\s]*) -> ([^\s]*)")

    if m := assign_re.match(command):
        return Command("ASSIGN", m.group(1), None, m.group(2))
    elif m := not_re.match(command):
        return Command("NOT", m.group(1), None, m.group(2))
    elif m := other_re.match(command):
        return Command(m.group(2), m.group(1), m.group(3), m.group(4))

    raise Exception(f"Unparseable command {command}")


def parse_commands(commands: list[str]) -> list[Command]:

    return [parse_command(command) for command in commands]


def test_one(input: list[str]) -> int:
    return Machine(parse_commands(input)).evaluate("i")


def part_one(input: list[str]) -> int:
    return Machine(parse_commands(input)).evaluate("a")


def test_two(input: list[str]) -> int:
    machine = Machine(parse_commands(input))
    machine.machine["y"] = Command("ASSIGN", 42, None, "y")

    return machine.evaluate("i")


def part_two(input: list[str]) -> int:
    machine = Machine(parse_commands(input))
    machine.machine["b"] = Command("ASSIGN", 16076, None, "b")

    return machine.evaluate("a")


if __name__ == "__main__":
    day = au.Day(
        2015,
        7,
        test_one,
        test_two,
        part_one,
        part_two,
        input=au.Day.InType.INPUT_MULTI_LINE_STR,
        test_input=[
            [
                "123 -> x",
                "456 -> y",
                "x AND y -> d",
                "x OR y -> e",
                "x LSHIFT 2 -> f",
                "y RSHIFT 2 -> g",
                "NOT x -> h",
                "NOT y -> i",
            ]
        ],
    )

    day.run_all(run_tests=True)
