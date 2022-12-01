from functools import cache
from typing import Generator, Optional

import aoc_utils as au

Rule = tuple[str, str]
RuleSet = tuple[Rule, ...]


def count_rules(input: str, rules: RuleSet) -> int:
    unique = set()

    for source, target in rules:
        start = 0
        while (found := input.find(source, start)) >= 0:
            unique.add(input[0:found] + target + input[found + len(source) :])
            start = found + 1

    return len(unique)


def test_one(input: str) -> int:
    rules: RuleSet = (("H", "HO"), ("H", "OH"), ("O", "HH"))

    return count_rules(input, rules)


def part_one(input: list[Rule | str]) -> int:
    rules: RuleSet = tuple(inp for inp in input if type(inp) == tuple)

    if type(input[-1]) != str:
        raise Exception("Bad input!")

    return count_rules(input[-1], rules)


def apply_rule(instring: str, source: str, target: str) -> Generator[str, None, None]:
    start = 0
    while (found := instring.find(source, start)) >= 0:
        candidate = instring[0:found] + target + instring[found + len(source) :]
        yield candidate
        start = found + 1


@cache
def apply_rule_list(instring: str, source: str, target: str) -> list[str]:
    return list(apply_rule(instring, source, target))


def find_molecule2(final_target: str, rules: RuleSet) -> int:
    molecules = set(["e"])
    step = 1
    while len(molecules) > 0:
        new_molecules = set()
        for molecule in molecules:
            for source, target in rules:
                for candidate in apply_rule(molecule, source, target):
                    if candidate == final_target:
                        return step

                    new_molecules.add(candidate)

        molecules = new_molecules
        print(f"Step {step} completed")
        step += 1

    raise Exception("Molecule not found")


def find_molecule(
    final_target: str, rules: RuleSet, seed: str = "e", step: int = 1
) -> Optional[int]:

    molecules = set()
    molecules.add(final_target)
    while len(molecules) > 0:
        new_molecules = set()
        for molecule in molecules:
            for source, target in rules:
                for candidate in apply_rule(molecule, target, source):
                    if candidate != molecule:
                        if candidate == seed:
                            return step

                        new_molecules.add(candidate)

        molecules = new_molecules
        print(f"Step {step} completed [{len(molecules)}")
        step += 1

    raise Exception("Molecule not found")


def test_two(input: str) -> int:
    rules: RuleSet = sorted(
        (("e", "H"), ("e", "O"), ("H", "HO"), ("H", "OH"), ("O", "HH")),
        key=lambda x: len(x[1]),
        reverse=True,
    )
    rc = find_molecule2(input, rules)
    if type(rc) == int:
        return rc

    raise Exception("ohnoe")


def part_two(input: list[Rule | str]) -> int:
    rules: RuleSet = tuple(inp for inp in input if type(inp) == tuple)

    if type(input[-1]) != str:
        raise Exception("Bad input!")

    rc = find_molecule2(input[-1], rules)
    if type(rc) == int:
        return rc

    raise Exception("ohnoe")


if __name__ == "__main__":
    molecule_parser = au.RegexParser(
        [(r"(.*) => (.*)", lambda m: (m[0], m[1])), (r"(.*)", lambda m: m[0])]
    )

    day = au.Day(
        2015,
        19,
        test_one,
        test_two,
        part_one,
        part_two,
        input=molecule_parser,
        test_input=["HOH", "HOHOHO"],
    )

    day.run_all(run_tests=True)
