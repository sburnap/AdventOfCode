from typing import Any, Callable
import pathlib
import datetime
from enum import Enum

AocFunction = Callable[[str], int]


class Day:
    InType = Enum("InType", ["INPUT_ONE_LINE_STR", "INPUT_MULTI_LINE_STR"])

    def __init__(
        self,
        year: int,
        day: int,
        test_one: AocFunction,
        test_two: AocFunction,
        part_one: AocFunction,
        part_two: AocFunction,
        test_input: Any,
        input=InType.INPUT_ONE_LINE_STR,
    ):
        self.year = year
        self.day = day
        self.dir = pathlib.Path(f"Advent{self.year}", f"Day{self.day}")
        self.test_input = test_input
        self.input = input
        self.test_one = test_one
        self.test_two = test_two
        self.part_one = part_one
        self.part_two = part_two

    def multi_line_input(self):
        return [line.strip() for line in open(self.dir / "input.txt")]

    def one_line_input(self):
        input = self.multi_line_input()
        assert len(input) == 1
        return input[0]

    def header(self):
        print()
        print(f"Advent of code for Year {self.year} Day {self.day}:")
        print()

    def test_it(self, fn) -> None:

        if type(self.test_input) == list:
            for input in self.test_input:
                start = datetime.datetime.now()
                answer = fn(input)
                elapsed = datetime.datetime.now() - start
                print(
                    f"({elapsed}) Test: {answer if answer is not None else 'None':<10} <- [ {input} ]"[
                        :100
                    ]
                )
            print()

    def run_it(self, fn, name: str) -> None:
        match self.input:
            case self.InType.INPUT_ONE_LINE_STR:
                start = datetime.datetime.now()
                answer = fn(self.one_line_input())
                elapsed = datetime.datetime.now() - start

            case self.InType.INPUT_MULTI_LINE_STR:
                start = datetime.datetime.now()
                answer = fn(self.multi_line_input())
                elapsed = datetime.datetime.now() - start

            case _:
                start = datetime.datetime.now()
                answer = fn(self.input)
                elapsed = datetime.datetime.now() - start

        print(f"({elapsed}) Answer for {name} is {answer}")

    def run_all(self, run_tests=False):
        self.header()
        if run_tests:
            self.test_it(self.test_one)
        self.run_it(self.part_one, "Part One")
        print()
        if run_tests:
            self.test_it(self.test_two)
        self.run_it(self.part_two, "Part Two")
