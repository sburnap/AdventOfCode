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

    def make_path(
        self, target: "Valve", valves: dict[str, "Valve"], timeleft: int
    ) -> list["Valve"]:
        if target.name not in self.paths:

            worklist: list[list["Valve"]] = [[self]]

            while len(worklist) > 0:
                workitem = worklist.pop(0)
                self.paths[target.name] = workitem + [target]
                target.paths[self.name] = [target] + workitem[::-1]
                if target.name in workitem[-1].tunnels:
                    break
                else:
                    if len(workitem) < timeleft:
                        for dest in workitem[-1].tunnels:
                            worklist.append(workitem + [valves[dest]])

        return self.paths[target.name]

    def __hash__(self):
        return hash(f"{self.name}:{self.flow}:{self.tunnels}")

    def __repr__(self):
        return f"{self.name} ({self.flow})"


def score(path: list[Valve], timeleft: int) -> int:
    if len(path) + 1 > timeleft:
        return 0
    return (
        max(0, (timeleft - len(path)) * path[-1].flow) * len(path[-1].tunnels)
    ) // len(path)


def nextone(
    start: Valve, valves: dict[str, Valve], targets: set[Valve], timeleft: int
) -> tuple[Optional[Valve], int]:

    potentials = [start.make_path(target, valves, timeleft) for target in targets]

    highscore = 0
    high: Optional[list[Valve]] = None
    for potential in potentials:
        sc = score(potential, timeleft)
        if sc > highscore:
            highscore = sc
            high = potential
            print(sc, potential)

    print("--")
    return high[-1] if high else None, timeleft - len(potential) + 1


def make_order(
    valves: dict[str, Valve], targets: set[Valve]
) -> Generator[Valve, None, None]:

    current: Optional[Valve] = valves["AA"]
    timeleft = 30
    while len(targets) > 0 and timeleft > 0:
        if current:
            current, timeleft = nextone(current, valves, targets, timeleft)
        if not current:
            break
        yield current
        targets.discard(current)


def score_order(order: list[Valve], valves: dict[str, Valve]) -> int:
    timeleft = 30
    releasing = 0
    pressure = 0
    current = valves["AA"]
    while timeleft > 0 and len(order) > 0:
        path = current.make_path(order.pop(0), valves, timeleft)
        if len(path) + 1 < timeleft:
            pressure += releasing * len(path)
            timeleft -= len(path)
            releasing += path[-1].flow
            # pressure += releasing
            print(f"Release {path[-1].name} at {30-timeleft}")
            current = path[-1]
        else:
            break

    pressure += releasing * timeleft
    return pressure


def walk(
    path: list[Valve],
    valves: dict[str, Valve],
    targets: set[Valve],
    timeleft: int,
) -> int:
    potentials = [
        path[-1].make_path(target, valves, timeleft)
        for target in targets
        if target not in path
    ]
    amount = 0
    mx = 0
    for potential in potentials:
        if len(potential) + 1 < timeleft:
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

    amount = walk([valves["AA"]], valves, targets, 30)
    print(amount)
    return 0


def part_one(input: list[Valve]) -> Optional[int]:

    valves = {valve.name: valve for valve in input}
    targets = set([valve for valve in input if valve.flow > 0])

    for _ in range(10):
        valves = {valve.name: valve for valve in input}
        targets = set([valve for valve in input if valve.flow > 0])

        amount = walk([valves["AA"]], valves, targets, 30)
        print(amount)
    return None


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
