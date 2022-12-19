from typing import Optional, Generator, Iterable
from dataclasses import dataclass
from collections import Counter

import aoc_utils as au


@dataclass
class Side:
    x: int
    y: int
    z: int
    angle: int

    def __hash__(self):
        return hash(f"{self.x},{self.y},{self.z}, {self.angle}")


@dataclass
class Cube:
    x: int
    y: int
    z: int

    def __hash__(self):
        return hash(f"{self.x},{self.y},{self.z}")

    def side_gen(self) -> Generator[Side, None, None]:
        yield Side(self.x, self.y, self.z, 0)
        yield Side(self.x + 1, self.y, self.z, 0)
        yield Side(self.x, self.y, self.z, 1)
        yield Side(self.x, self.y + 1, self.z, 1)
        yield Side(self.x, self.y, self.z, 2)
        yield Side(self.x, self.y, self.z + 1, 2)


def make_faces(cubes: Iterable[Cube]) -> set[Side]:
    faces: Counter = Counter()

    for cube in cubes:
        for side in cube.side_gen():
            faces[side] += 1

    return set([face for face in faces if faces[face] == 1])


def test_one(cubes: list[Cube]) -> Optional[int]:
    return len(make_faces(cubes))


def part_one(cubes: list[Cube]) -> Optional[int]:
    return len(make_faces(cubes))


def adjacent(
    cube: Cube, minx: int, miny: int, minz: int, maxx: int, maxy: int, maxz: int
) -> Generator[Cube, None, None]:
    if cube.x < maxx:
        yield Cube(cube.x + 1, cube.y, cube.z)
    if cube.x > minx:
        yield Cube(cube.x - 1, cube.y, cube.z)
    if cube.y < maxy:
        yield Cube(cube.x, cube.y + 1, cube.z)
    if cube.y > miny:
        yield Cube(cube.x, cube.y - 1, cube.z)
    if cube.z < maxz:
        yield Cube(cube.x, cube.y, cube.z + 1)
    if cube.z > minz:
        yield Cube(cube.x, cube.y, cube.z - 1)


def find_outer_faces(cubes: set[Cube]) -> int:
    minx = miny = minz = 99
    maxx = maxy = maxz = 0
    for cube in cubes:
        minx = min(minx, cube.x)
        miny = min(miny, cube.y)
        minz = min(minz, cube.z)
        maxx = max(maxx, cube.x)
        maxy = max(maxy, cube.y)
        maxz = max(maxz, cube.z)
    minx -= 1
    miny -= 1
    minz -= 1
    maxx += 1
    maxy += 1
    maxz += 1

    faces = make_faces(cubes)
    outerfaces: set[Side] = set()

    workitems = [Cube(minx, miny, minz)]
    while len(workitems) > 0:
        workcube = workitems.pop(0)
        for testcube in adjacent(workcube, minx, miny, minz, maxx, maxy, maxz):
            if testcube not in cubes:
                cubes.add(testcube)
                workitems.append(testcube)
                for side in testcube.side_gen():
                    if side in faces:
                        outerfaces.add(side)

    return len(outerfaces)


def test_two(cubes: list[Cube]) -> Optional[int]:

    return find_outer_faces(set(cubes))


def part_two(cubes: list[Cube]) -> Optional[int]:
    return find_outer_faces(set(cubes))


if __name__ == "__main__":
    cube_parser = au.RegexParser(
        [
            (r"^(\d*),(\d*),(\d*)", lambda m: Cube(int(m[0]), int(m[1]), int(m[2]))),
        ]
    )
    day = au.Day(
        2022,
        18,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=cube_parser,
        input=cube_parser,
    )

    day.run_all(run_tests=True)
