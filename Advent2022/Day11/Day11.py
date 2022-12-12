from typing import Optional
from functools import reduce
from dataclasses import dataclass
import operator

import aoc_utils as au


@dataclass
class Items:
    items: list


@dataclass
class Operation:
    op: str
    target: str | int


@dataclass
class Divisor:
    val: int


@dataclass
class Test:
    test: str
    target: int


class Monkey:
    def __init__(
        self,
        number: int,
    ):
        self.number = number
        self.items: list[int]
        self.op: Operation
        self.divisor: int
        self.truetarget: int
        self.falsetarget: int
        self.inspect = 0

    def inspect_item(self, item: int) -> int:
        self.inspect += 1

        match self.op.target:
            case str():
                val = item
            case int() as i:
                val = i

        match self.op.op:
            case "+":
                return item + val
            case "*":
                return item * val
            case _:
                raise Exception(f"Bad opcode {self.op.op} encountered")

    def target(self, worry: int) -> int:
        return self.truetarget if worry % self.divisor == 0 else self.falsetarget

    def add_item(self, worry: int) -> None:
        self.items.append(worry)

    def __repr__(self):
        return f"Monkey {self.number} has {self.items}"


def get_monkeys(
    input: list[int | Items | Operation | Divisor],
) -> tuple[list[Monkey], int]:
    monkeys: list[Monkey] = []

    divisors: list[int] = []

    for inp in input:
        match inp:
            case int() as n:
                monkeys.append(Monkey(n))

            case Items() as items:
                monkeys[-1].items = items.items

            case Divisor() as divisor:
                monkeys[-1].divisor = divisor.val
                divisors.append(divisor.val)

            case Operation() as operation:
                monkeys[-1].op = operation

            case Test() as test:
                if test.test == "true":
                    monkeys[-1].truetarget = test.target
                elif test.test == "false":
                    monkeys[-1].falsetarget = test.target

    return monkeys, reduce(operator.mul, divisors, 1)


def do_tossing(
    input: list[int | Items | Operation | Divisor],
    rounds: int,
    worry_div: Optional[int] = None,
) -> int:
    monkeys, modulo = get_monkeys(input)

    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.items:
                worry = monkey.inspect_item(monkey.items.pop())

                if worry_div:
                    worry = worry // worry_div
                else:
                    worry %= modulo

                monkeys[monkey.target(worry)].add_item(worry)

    inspects = sorted(monkey.inspect for monkey in monkeys)
    return inspects[-1] * inspects[-2]


# expect 10605
def test_one(input: list[int | Items | Operation | Divisor]) -> Optional[int]:
    return do_tossing(input, 20, 3)


# expect 58794
def part_one(input: list[int | Items | Operation | Divisor]) -> Optional[int]:
    return do_tossing(input, 20, 3)


# expect 2713310158
def test_two(input: list[int | Items | Operation | Divisor]) -> Optional[int]:
    return do_tossing(input, 10000)


# expect 20151213744
def part_two(input: list[int | Items | Operation | Divisor]) -> Optional[int]:
    return do_tossing(input, 10000)


if __name__ == "__main__":
    monkey_parser = au.RegexParser(
        [
            ("^Monkey (\d*):$", lambda m: int(m[0])),
            (
                "^\s*Starting items: (.*)$",
                lambda m: Items([int(n) for n in m[0].split(",")]),
            ),
            ("^\s*Operation: new = old (.) old$", lambda m: Operation(m[0], "old")),
            (
                "^\s*Operation: new = old (.) (.*)$",
                lambda m: Operation(m[0], int(m[1])),
            ),
            ("^\s*Test: divisible by (.*)$", lambda m: Divisor(int(m[0]))),
            (
                "^\s*If (true|false): throw to monkey (.*)$",
                lambda m: Test(m[0], int(m[1])),
            ),
            ("\s*", lambda m: ""),
        ]
    )
    day = au.Day(
        2022,
        11,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=monkey_parser,
        input=monkey_parser,
    )

    day.run_all(run_tests=True)
