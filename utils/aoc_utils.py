from typing import Any, Callable, Union, Optional, Tuple
import pathlib
import datetime
import re
from enum import Enum
from os.path import exists
from datetime import timedelta

TestFunction = Union[
    Callable[[list[Any]], Optional[str | int]],
    Callable[[str], Optional[str | int]],
    Callable[[int], Optional[str | int]],
]


AnswerFunction = Union[
    Callable[[list[Any]], Optional[str | int]],
    Callable[[str], Optional[str | int]],
    Callable[[int], Optional[str | int]],
]
FormFunction = Callable[[list[str]], Any]
Map = list[list[str]]


class RegexException(Exception):
    pass


class ParsingException(Exception):
    pass


class Parser:
    def parse(self, line: str, strip: bool = True) -> Any:
        if strip:
            return line.strip()

        return line


class OneLineParser(Parser):
    def parse(self, line: str, strip: bool = True) -> Any:
        if strip:
            return line.strip()

        return line


class IntParser(Parser):
    def parse(self, line: str, strip: bool = True) -> Any:
        return int(line.strip())


class MapParser(Parser):
    def __init__(self, integer=False):
        self.integer = integer

    def parse(self, line, strip: bool = True) -> list[int | str]:
        if self.integer:
            return [int(ch) for ch in line.strip()]
        else:
            return [ch for ch in line.strip()]


class RegexParser(Parser):
    def __init__(self, regexes: list[tuple[str, Optional[FormFunction]]]):
        self.regexes = [(re.compile(regex[0]), regex[1]) for regex in regexes]

    def parse(self, line, strip: bool = True) -> Any:
        for regex, form in self.regexes:
            if m := regex.match(line):
                if form:
                    return form(list(m.groups()))
                else:
                    return m.groups()

        raise RegexException(f"Could not parse '{line}'")

    def _form(self, results: tuple) -> Any:
        return results


class Day:
    def __init__(
        self,
        year: int,
        day: int,
        test_one: Optional[TestFunction],
        test_two: Optional[TestFunction],
        part_one: AnswerFunction,
        part_two: AnswerFunction,
        test_input: Optional[list[str] | str | int | Parser] = None,
        input: list[str] | str | int | Parser = Parser(),
    ):
        self.year = year
        self.day = day
        self.dir = pathlib.Path(f"Advent{self.year}", f"Day{self.day}")
        self.input = input
        self.test_input = test_input if test_input else self.input
        self.test_one = test_one
        self.test_two = test_two
        self.part_one = part_one
        self.part_two = part_two

    def multi_line_input(self, filename="input.txt", parser: Parser = Parser()):
        try:
            rc = []

            for i, line in enumerate(open(self.dir / filename)):
                if (parsed := parser.parse(line)) != None:
                    rc.append(parsed)
            return rc

        except RegexException as ex:
            raise ParsingException(
                f"Parse filed in {filename} on line {i}: {ex}"
            ) from ex

    def header(self):
        print()
        print(f"Advent of code for Year {self.year} Day {self.day}:")
        print()

    def runner(
        self, fn, infile: str, input_method: str | int | list[str] | Parser
    ) -> tuple[Any, timedelta]:
        match input_method:
            case [*input]:
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

            case str(input) | int(input):
                start = datetime.datetime.now()
                answer = fn(input)
                elapsed = datetime.datetime.now() - start

            case OneLineParser():
                start = datetime.datetime.now()
                answer = fn(
                    self.multi_line_input(filename=infile, parser=input_method)[0]
                )
                elapsed = datetime.datetime.now() - start

            case Parser():
                start = datetime.datetime.now()
                answer = fn(self.multi_line_input(filename=infile, parser=input_method))
                elapsed = datetime.datetime.now() - start

            case _:
                raise ParsingException(f"Unknown data input type {input_method}")
        return answer, elapsed

    def test_it(self, fn, filename="test_input.txt") -> None:
        if fn:
            answer, elapsed = self.runner(fn, filename, self.test_input)
            if answer:
                print(f"({elapsed}) Test is {answer if answer else 'I Dunno'}")

    def run_it(self, fn, name: str) -> None:
        answer, elapsed = self.runner(fn, "input.txt", self.input)
        print(f"({elapsed}) Answer for {name} is {answer if answer else 'I Dunno'}")

    def run_all(self, run_tests=False):
        self.header()
        if run_tests:
            self.test_it(self.test_one)
        self.run_it(self.part_one, "Part One")
        print()
        if run_tests:
            self.test_it(
                self.test_two,
                filename="test_input2.txt"
                if exists(self.dir / "test_input2.txt")
                else "test_input.txt",
            )
        self.run_it(self.part_two, "Part Two")
