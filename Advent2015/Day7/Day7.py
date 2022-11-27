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

    def __repr__(self):
        if self.operand2:
            return f"{self.name} {self.operand1}, {self.operand2} -> {self.target}"
        else:
            return f"{self.name} {self.operand1} -> {self.target}"


class Machine:
    def __init__(self, command_list: list[Command]):
        self.machine = {command.target: command for command in command_list}

    @cache
    def evaluate(self, wire: str) -> int:
        command: Command = self.machine[wire]

        op1 = (
            command.operand1
            if type(command.operand1) == int
            else self.evaluate(command.operand1)
        )
        op2 = (
            command.operand2
            if type(command.operand2) == int or command.operand2 == None
            else self.evaluate(command.operand2)
        )

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


def test_one(input: list[str]) -> int:
    return Machine(input).evaluate("i")


# expected 16076
def part_one(input: list[str]) -> int:
    return Machine(input).evaluate("a")


def test_two(input: list[str]) -> int:
    machine = Machine(input)
    machine.machine["y"] = Command("ASSIGN", 42, None, "y")

    return machine.evaluate("i")


# expected 2797
def part_two(input: list[str]) -> int:
    machine = Machine(input)
    machine.machine["b"] = Command("ASSIGN", 16076, None, "b")

    return machine.evaluate("a")


if __name__ == "__main__":
    wire_parser = au.RegexParser(
        [
            ("([^\s]*) -> ([^\s]*)", lambda m: Command("ASSIGN", m[0], None, m[1])),
            ("NOT ([^\s]*) -> ([^\s]*)", lambda m: Command("NOT", m[0], None, m[1])),
            (
                "([^\s]*) (AND|OR|LSHIFT|RSHIFT) ([^\s]*) -> ([^\s]*)",
                lambda m: Command(m[1], m[0], m[2], m[3]),
            ),
        ]
    )
    day = au.Day(
        2015,
        7,
        test_one,
        test_two,
        part_one,
        part_two,
        input=wire_parser,
        test_input=wire_parser,
    )

    day.run_all(run_tests=True)
