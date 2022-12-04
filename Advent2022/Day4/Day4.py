import aoc_utils as au

Area = tuple[int, int]


def contains(first: Area, second: Area) -> bool:
    return (first[0] <= second[0] and first[-1] >= second[-1]) or (
        second[0] <= first[0] and second[-1] >= first[-1]
    )


def test_one(input: list[tuple[Area, Area]]) -> int:
    return len([pair for pair in input if contains(*pair)])


def part_one(input: list[tuple[Area, Area]]) -> int:
    return len([pair for pair in input if contains(*pair)])


def overlap(first: Area, second: Area) -> bool:
    return (second[0] <= first[0] <= second[-1]) or (first[0] <= second[0] <= first[-1])


def test_two(input: list[tuple[Area, Area]]) -> int:
    return len([pair for pair in input if overlap(*pair)])


def part_two(input: list[tuple[Area, Area]]) -> int:
    return len([pair for pair in input if overlap(*pair)])


if __name__ == "__main__":
    pair_parser = au.RegexParser(
        [
            (
                "(\d*)-(\d*),(\d*)-(\d*)",
                lambda m: ((int(m[0]), int(m[1])), (int(m[2]), int(m[3]))),
            )
        ]
    )
    day = au.Day(
        2022,
        4,
        test_one,
        test_two,
        part_one,
        part_two,
        input=pair_parser,
        test_input=pair_parser,
    )

    day.run_all(run_tests=True)
