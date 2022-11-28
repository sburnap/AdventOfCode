from typing import Generator

import aoc_utils as au


def print_map(map: au.Map) -> None:

    for row in map:
        print("".join(row))


DEBUG = False


def adjacent(
    x: int, y: int, width: int, height: int
) -> Generator[tuple[int, int], None, None]:

    if x > 0:
        if y > 0:
            yield x - 1, y - 1
        yield x - 1, y
        if y < height - 1:
            yield x - 1, y + 1

    if y > 0:
        yield x, y - 1
    if y < height - 1:
        yield x, y + 1

    if x < width - 1:
        if y > 0:
            yield x + 1, y - 1
        yield x + 1, y
        if y < height - 1:
            yield x + 1, y + 1


def neighbors(map: au.Map, x: int, y: int) -> int:

    return len(
        [
            map[ay][ax]
            for ax, ay in adjacent(x, y, len(map[0]), len(map))
            if map[ay][ax] == "#"
        ]
    )


def will_live(map: au.Map, x: int, y: int) -> bool:
    neigh = neighbors(map, x, y)
    if map[y][x] == "#" and neigh == 2:
        return True

    return neigh == 3


def time_step(map: au.Map) -> au.Map:
    return [
        ["#" if will_live(map, x, y) else "." for x in range(len(map[0]))]
        for y in range(len(map))
    ]


def lights_on(map: au.Map) -> int:
    return sum(
        [
            sum([1 if map[y][x] == "#" else 0 for x in range(len(map[0]))])
            for y in range(len(map))
        ]
    )


def test_one(map: au.Map) -> int:
    if DEBUG:
        print_map(map)

    for step in range(4):
        map = time_step(map)
        if DEBUG:
            print()
            print(f"After {step+1} steps:")
            print_map(map)
    return lights_on(map)


# expected 814
def part_one(map: au.Map) -> int:
    for step in range(100):
        map = time_step(map)
    return lights_on(map)


def pin_corners(map: au.Map) -> au.Map:
    newmap = map
    newmap[0][0] = "#"
    newmap[len(newmap[0]) - 1][0] = "#"
    newmap[0][len(newmap) - 1] = "#"
    newmap[len(newmap[0]) - 1][len(newmap) - 1] = "#"

    return newmap


def time_step2(map: au.Map) -> au.Map:
    return pin_corners(
        [
            ["#" if will_live(map, x, y) else "." for x in range(len(map[0]))]
            for y in range(len(map))
        ]
    )


def test_two(map: au.Map) -> int:
    map = pin_corners(map)
    if DEBUG:
        print_map(map)

    for step in range(5):
        map = time_step2(map)
        if DEBUG:
            print()
            print(f"After {step+1} steps:")
            print_map(map)
    return lights_on(map)


# expected 924
def part_two(map: au.Map) -> int:
    map = pin_corners(map)

    for _ in range(100):
        map = time_step2(map)
    return lights_on(map)


if __name__ == "__main__":
    day = au.Day(
        2015,
        18,
        test_one,
        test_two,
        part_one,
        part_two,
        input=au.Day.InType.INPUT_MAP,
        test_input=au.Day.InType.INPUT_MAP,
    )

    day.run_all(run_tests=True)
