from typing import Any
import pathlib


class Day:
    INPUT_ONE_LINE_STR = 1

    def __init__(
        self,
        year: int,
        day: int,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input: Any,
        input=INPUT_ONE_LINE_STR,
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

    def one_line_input(self):
        return open(self.dir / "input.txt").readlines()[0]

    def header(self):
        print()
        print(f"Advent of code for Year {self.year} Day {self.day}:")
        print()

    def test_it(self, fn) -> None:

        if type(self.test_input) == list:
            for input in self.test_input:
                answer = fn(self, input)
                print(
                    f"Test: {answer if answer is not None else 'None':<10} <- [ {input} ]"
                )

    def run_it(self, fn, name: str) -> None:
        match self.input:
            case self.INPUT_ONE_LINE_STR:
                answer = fn(self)

        print(f"Answer for {name} is {answer}")

    def run_all(self, run_tests=False):
        self.header()
        if run_tests:
            self.test_it(self.test_one)
        self.run_it(self.part_one, "Part One")
        if run_tests:
            self.test_it(self.test_two)
        self.run_it(self.part_two, "Part Two")
