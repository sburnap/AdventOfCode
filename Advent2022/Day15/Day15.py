from typing import Optional, Generator
from dataclasses import dataclass

import aoc_utils as au


@dataclass
class Point:
    x: int
    y: int


def distance(point1: Point, point2: Point) -> int:
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)


class Sensor:
    def __init__(self, sensor: Point, beacon: Point):
        self.sensor = sensor
        self.beacon = beacon
        self.range = distance(self.sensor, self.beacon)

    def __repr__(self):
        return (
            f"Sensor {self.sensor.x},{self.sensor.y}, "
            f"Beacon {self.beacon.x},{self.beacon.y} range {self.range}"
        )

    def range_covered(self, y: int) -> tuple[int, int]:
        yoffset = abs(y - self.sensor.y)
        ycover = self.range - yoffset
        if ycover > 0:
            return self.sensor.x - ycover, self.sensor.x + ycover
        else:
            return 0, 0


def get_ranges(
    sensors: list[Sensor],
    row: int,
    low: Optional[int] = None,
    high: Optional[int] = None,
) -> list[tuple[int, int]]:
    coverages = sorted([sensor.range_covered(row) for sensor in sensors])
    merged: list[tuple[int, int]] = []
    for coverage in coverages:
        if coverage != (0, 0):
            if low is not None and coverage[0] < low:
                coverage = (low, coverage[1])
            if high is not None and coverage[1] > high:
                coverage = (coverage[0], high)
            if len(merged) == 0:
                merged.append(coverage)
            else:
                if merged[-1][1] >= coverage[0] - 1:
                    if merged[-1][1] < coverage[1]:
                        merged[-1] = (merged[-1][0], coverage[1])
                else:
                    merged.append(coverage)
    return merged


def find_beacon(sensors: list[Sensor], low: int, high: int) -> Optional[int]:
    for row in range(low, high):
        merged = get_ranges(sensors, row, low, high)
        if len(merged) == 2:
            x = merged[0][1] + 1
            y = row
            print(y)
            return (x * 4000000) + y
    return None


def num_hidden(
    sensors: list[Sensor],
    row: int,
    low: Optional[int] = None,
    high: Optional[int] = None,
) -> Optional[int]:
    merged = get_ranges(sensors, row, low, high)
    return sum(m[1] - m[0] for m in merged)


def test_one(input: list[tuple[Point, Point]]) -> Optional[int]:
    return num_hidden([Sensor(sensor, beacon) for sensor, beacon in input], 10)


def part_one(input: list[tuple[Point, Point]]) -> Optional[int]:
    return num_hidden([Sensor(sensor, beacon) for sensor, beacon in input], 2000000)


def test_two(input: list[tuple[Point, Point]]) -> Optional[int]:
    return find_beacon([Sensor(sensor, beacon) for sensor, beacon in input], 0, 20)


def part_two(input: list[tuple[Point, Point]]) -> Optional[int]:
    return find_beacon([Sensor(sensor, beacon) for sensor, beacon in input], 0, 4000000)


if __name__ == "__main__":
    beacon_parser = au.RegexParser(
        [
            (
                r"^Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)$",
                lambda m: (Point(int(m[0]), int(m[1])), Point(int(m[2]), int(m[3]))),
            )
        ]
    )
    day = au.Day(
        2022,
        15,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=beacon_parser,
        input=beacon_parser,
    )

    day.run_all(run_tests=True)
