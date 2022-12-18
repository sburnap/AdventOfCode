from typing import Optional, Generator
from dataclasses import dataclass
from functools import lru_cache

import aoc_utils as au


@dataclass
class TunnelDef:
    source: str
    destinations: list[str]


class Valve:
    def __init__(self, name: str, flow: int, tunnels: list[str]):
        self.name = name
        self.flow = flow
        self.tunnels = tunnels
        self.paths: dict[str, list["Valve"]] = {}

    def make_path(self, target: "Valve", valves: dict[str, "Valve"]) -> list["Valve"]:
        if target.name in self.paths:
            return self.paths[target.name]

        worklist: list[list["Valve"]] = [[self]]

        while len(worklist) > 0:
            workitem = worklist.pop(0)
            self.paths[target.name] = workitem + [target]
            target.paths[self.name] = [target] + workitem[::-1]
            if target.name in workitem[-1].tunnels:
                return self.paths[target.name]
            else:
                for dest in workitem[-1].tunnels:
                    worklist.append(workitem + [valves[dest]])

        raise Exception(f"No path found from {self.name} to {target.name}")

    def __repr__(self):
        return f"{self.name} ({self.flow})"


def walk(
    path: list[Valve],
    valves: dict[str, Valve],
    targets: set[Valve],
    timeleft: int,
) -> int:
    potentials = [
        path[-1].make_path(target, valves) for target in targets if target not in path
    ]
    mx = 0
    for potential in potentials:
        if len(potential) < timeleft:
            newtimeleft = timeleft - (len(potential))
            amount = (
                walk(path + [potential[-1]], valves, targets, newtimeleft)
                + potential[-1].flow * newtimeleft
            )
            if amount > mx:
                mx = amount
    return mx


def test_one(input: list[Valve]) -> Optional[int]:
    valves = {valve.name: valve for valve in input}
    targets = set([valve for valve in input if valve.flow > 0])

    return walk([valves["AA"]], valves, targets, 30)


def part_one(input: list[Valve]) -> Optional[int]:

    valves = {valve.name: valve for valve in input}
    targets = set([valve for valve in input if valve.flow > 0])

    return walk([valves["AA"]], valves, targets, 30)


def test_two(input: list[Valve]) -> Optional[int]:
    return None


def part_two(input: list[Valve]) -> Optional[int]:
    return None


if __name__ == "__main__":
    valve_parser = au.RegexParser(
        [
            (
                r"^Valve (.*) has flow rate=(\d*); tunnels? leads? to valves? (.*)$",
                lambda m: (Valve(name=m[0], flow=int(m[1]), tunnels=m[2].split(", "))),
            )
        ]
    )
    day = au.Day(
        2022,
        16,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=valve_parser,
        input=valve_parser,
    )

    day.run_all(run_tests=True)
