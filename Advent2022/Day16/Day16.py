from typing import Optional, Generator


import aoc_utils as au


class Valve:
    def __init__(self, name: str, flow: int, tunnels: list[str]):
        self.name = name
        self.flow = flow
        self.tunnels = {tunnel: 1 for tunnel in tunnels}
        self.paths: dict[str, list["Valve"]] = {}

    def __repr__(self):
        return f"{self.name} ({self.flow})"


def score(valve: Valve, valves: dict[Valve], time: int, seen: list[str]) -> None:
    if time < 1:
        return 0

    rc = 0
    for tunnel in valve.tunnels:
        if tunnel not in seen:
            rc += score(valves[tunnel], valves, time - 2, seen + [valve.name])

    valve.score = rc + valve.flow * time
    return valve.score


def test_one(input: list[Valve]) -> Optional[int]:
    valves = {valve.name: valve for valve in input}

    score(valves["AA"], valves, 30, [])
    ticks = 30
    location = "AA"
    flow = 0

    return None


def part_one(input: list[Valve]) -> Optional[int]:
    valves = {valve.name: valve for valve in input}

    score(valves["AA"], valves, 30, [])
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
