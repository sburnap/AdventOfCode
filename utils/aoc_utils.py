from typing import Any, Callable, Union
import pathlib
import datetime
import re
from enum import Enum

TestFunction = Union[
    Callable[[list[str]], int],
    Callable[[str], int],
    Callable[[list[str]], str],
    Callable[[str], str],
]


AnswerFunction = Union[Callable[[list[str]], int], Callable[[str], int]]


class Parser:
    def parse(self, line) -> any:

        return line


class RegexParser(Parser):
    def __init__(self, regexes: list[str], form=None):
        self.regexes = [re.compile(regex) for regex in regexes]
        self.form = form if form else self._form

    def parse(self, line) -> any:

        for regex in self.regexes:
            if m := regex.match(line):
                return self.form(m.groups())

        raise Exception(f"Could not parse {line}")

    def _form(self, results: tuple) -> any:
        return results


class Day:
    InType = Enum("InType", ["INPUT_ONE_LINE_STR", "INPUT_MULTI_LINE_STR"])

    def __init__(
        self,
        year: int,
        day: int,
        test_one: TestFunction,
        test_two: TestFunction,
        part_one: AnswerFunction,
        part_two: TestFunction,
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

    def multi_line_input(self, filename="input.txt", parser: Parser = Parser()):
        return [parser.parse(line.strip()) for line in open(self.dir / filename)]

    def one_line_input(self, filename="input.txt"):
        input = self.multi_line_input(filename=filename)
        assert len(input) == 1
        return input[0]

    def header(self):
        print()
        print(f"Advent of code for Year {self.year} Day {self.day}:")
        print()

    def test_it(self, fn) -> None:

        if fn:
            match self.test_input:

                case [*input] | str(input):
                    if type(input) == str:
                        input = [input]
                    for line in input:
                        start = datetime.datetime.now()
                        answer = fn(line)
                        elapsed = datetime.datetime.now() - start
                        print(
                            f"({elapsed}) Test: {answer if answer is not None else 'None':<10} <- [ {line} ]"[
                                :100
                            ]
                        )
                    print()

                case Parser():
                    start = datetime.datetime.now()
                    answer = fn(
                        self.multi_line_input(
                            filename="test_input.txt", parser=self.test_input
                        )
                    )
                    elapsed = datetime.datetime.now() - start
                    print(f"({elapsed}) Test is {answer}")

                case self.InType.INPUT_ONE_LINE_STR:
                    start = datetime.datetime.now()
                    answer = fn(self.one_line_input(filename="test_input.txt"))
                    elapsed = datetime.datetime.now() - start
                    print(f"({elapsed}) Test is {answer}")

                case self.InType.INPUT_MULTI_LINE_STR:
                    start = datetime.datetime.now()
                    answer = fn(self.multi_line_input(filename="test_input.txt"))
                    elapsed = datetime.datetime.now() - start
                    print(f"({elapsed}) Test is {answer}")

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

            case Parser():
                start = datetime.datetime.now()
                answer = fn(self.multi_line_input(parser=self.test_input))
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
