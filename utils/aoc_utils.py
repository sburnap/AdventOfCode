from typing import Any, Callable, Union, Optional, Tuple
import pathlib
import datetime
import re
from enum import Enum
from datetime import timedelta

TestFunction = Union[
    Callable[[list[Any]], int],
    Callable[[str], int],
    Callable[[list[Any]], str],
    Callable[[str], str],
]


AnswerFunction = Union[Callable[[list[Any]], int], Callable[[str], int]]
FormFunction = Callable[[list[str]], Any]
Map = list[list[str]]


class Parser:
    def parse(self, line) -> Any:

        return line


class IntParser(Parser):
    def parse(self, line) -> Any:

        return int(line)


class MapParser(Parser):
    def parse(self, line) -> Any:

        return [ch for ch in line]


class RegexParser(Parser):
    def __init__(self, regexes: list[tuple[str, Optional[FormFunction]]]):
        self.regexes = [(re.compile(regex[0]), regex[1]) for regex in regexes]

    def parse(self, line) -> Any:

        for regex, form in self.regexes:
            if m := regex.match(line):
                if form:
                    return form(list(m.groups()))
                else:
                    return m.groups()

        raise Exception(f"Could not parse {line}")

    def _form(self, results: tuple) -> Any:
        return results


class Day:
    InType = Enum(
        "InType",
        [
            "INPUT_ONE_LINE_STR",
            "INPUT_MULTI_LINE_STR",
            "INPUT_MULTI_LINE_INT",
            "INPUT_MAP",
        ],
    )

    def __init__(
        self,
        year: int,
        day: int,
        test_one: Optional[TestFunction],
        test_two: Optional[TestFunction],
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

    def runner(self, fn, infile: str) -> tuple[Any, timedelta]:

        input: str | list[str]
        match self.test_input:
            # See https://github.com/python/mypy/issues/13950
            case [*input] | str(input):  # type: ignore[misc]
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
                answer = None

            case Parser():
                start = datetime.datetime.now()
                answer = fn(
                    self.multi_line_input(filename=infile, parser=self.test_input)
                )
                elapsed = datetime.datetime.now() - start

            case self.InType.INPUT_ONE_LINE_STR:
                start = datetime.datetime.now()
                answer = fn(self.one_line_input(filename=infile))
                elapsed = datetime.datetime.now() - start

            case self.InType.INPUT_MULTI_LINE_STR:
                start = datetime.datetime.now()
                answer = fn(self.multi_line_input(filename=infile))
                elapsed = datetime.datetime.now() - start

            case self.InType.INPUT_MULTI_LINE_INT:
                start = datetime.datetime.now()
                answer = fn(self.multi_line_input(parser=IntParser(), filename=infile))
                elapsed = datetime.datetime.now() - start

            case self.InType.INPUT_MAP:
                start = datetime.datetime.now()
                answer = fn(self.multi_line_input(parser=MapParser(), filename=infile))
                elapsed = datetime.datetime.now() - start

            case None:
                answer = fn(None)

            case _:
                raise Exception("Unknown data input type")
        return answer, elapsed

    def test_it(self, fn) -> None:
        if fn:
            answer, elapsed = self.runner(fn, "test_input.txt")
            print(f"({elapsed}) Test is {answer}")

    def run_it(self, fn, name: str) -> None:
        answer, elapsed = self.runner(fn, "input.txt")
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
