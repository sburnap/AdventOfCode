from typing import Optional
from dataclasses import dataclass

import aoc_utils as au


@dataclass
class VarRec:
    target: str
    value: int

    def evaluate(self, _: "References", ignore: Optional[str] = None) -> Optional[int]:
        return self.value if self.target != ignore else None

    def find_human(self, _: "References", target: int, _: str) -> int:
        return target


@dataclass
class OpRec:
    target: str
    left: str
    right: str
    operation: str

    def evaluate(
        self, references: "References", ignore: Optional[str] = None
    ) -> Optional[int]:
        if self.left in references and self.right in references:
            lhs = references[self.left].evaluate(references, ignore)
            rhs = references[self.right].evaluate(references, ignore)

            if lhs is None or rhs is None:
                return None

            match self.operation:
                case "*":
                    return lhs * rhs
                case "/":
                    return lhs // rhs
                case "+":
                    return lhs + rhs
                case "-":
                    return lhs - rhs

        raise Exception(f"I can't math {self.left} {self.operation} {self.right}")

    def find_human(self, references: "References", target: int, ignore: str) -> int:
        left = references.get(self.left)
        right = references.get(self.right)

        if left is not None and right is not None:
            lhs = left.evaluate(references, ignore)
            rhs = right.evaluate(references, ignore)

            if lhs is None:
                assert rhs is not None

                match self.operation:
                    case "*":
                        newtarget = target // rhs
                    case "/":
                        newtarget = target * rhs
                    case "+":
                        newtarget = target - rhs
                    case "-":
                        newtarget = target + rhs
                return left.find_human(references, newtarget, ignore)
            elif rhs is None:
                assert lhs is not None

                match self.operation:
                    case "*":
                        newtarget = target // lhs
                    case "/":
                        newtarget = target * lhs
                    case "+":
                        newtarget = target - lhs
                    case "-":
                        newtarget = lhs - target
                return right.find_human(references, newtarget, ignore)
        raise Exception(
            f"I can't math {self.left}({left}) {self.operation} {self.right}({right})"
        )


References = dict[str, VarRec | OpRec]


def test_one(monkeys: list[VarRec | OpRec]) -> Optional[int]:
    references: References = {monkey.target: monkey for monkey in monkeys}
    return references["root"].evaluate(references)


def part_one(monkeys: list[VarRec | OpRec]) -> Optional[int]:
    references: References = {monkey.target: monkey for monkey in monkeys}
    return references["root"].evaluate(references)


def balance_equation(monkeys: list[VarRec | OpRec]) -> int:
    references: References = {monkey.target: monkey for monkey in monkeys}

    root = references["root"]
    assert type(root) is OpRec
    assert type(references["humn"]) is VarRec

    left = references[root.left].evaluate(references, ignore="humn")
    right = references[root.right].evaluate(references, ignore="humn")

    if left is not None:
        answer = references[root.right].find_human(references, left, ignore="humn")
    elif right is not None:
        answer = references[root.left].find_human(references, right, ignore="humn")
    else:
        raise Exception("No humans here")

    references["humn"].value = answer
    assert references[root.right].evaluate(references) == references[
        root.left
    ].evaluate(references)
    return answer


def test_two(monkeys: list[VarRec | OpRec]) -> Optional[int]:
    return balance_equation(monkeys)


def part_two(monkeys: list[VarRec | OpRec]) -> Optional[int]:
    return balance_equation(monkeys)


if __name__ == "__main__":
    math_parser = au.RegexParser(
        [
            (r"^(.*): (\d*)$", lambda m: VarRec(m[0], int(m[1]))),
            (
                r"(.*): (.*) (\+|\-|\*|\/) (.*)$",
                lambda m: OpRec(m[0], m[1], m[3], m[2]),
            ),
        ]
    )
    day = au.Day(
        2022,
        21,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=math_parser,
        input=math_parser,
    )

    day.run_all(run_tests=True)
