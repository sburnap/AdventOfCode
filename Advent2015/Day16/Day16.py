import aoc_utils as au


mgcsam_data = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


# expected 103
def part_one(sues: list[tuple[int, dict[str, int]]]) -> int:
    for sue in sues:
        if all(mgcsam_data[item] == sue[1][item] for item in sue[1].keys()):
            return sue[0]

    raise Exception("No sue found")


def compareratizer(key: str, a: int, b: int):
    match key:
        case "cats" | "trees":
            return a < b
        case "pomeranians" | "goldfish":
            return a > b
        case _:
            return a == b


# expected 405
def part_two(sues: list[tuple[int, dict[str, int]]]) -> int:
    for sue in sues:
        if all(
            compareratizer(item, mgcsam_data[item], sue[1][item])
            for item in sue[1].keys()
        ):
            return sue[0]

    raise Exception("No sue found")


if __name__ == "__main__":
    sue_parser = au.RegexParser(
        [
            (
                r"Sue (\d*): (.*): (.*), (.*): (.*), (.*): (.*)",
                lambda m: (
                    int(m[0]),
                    {m[1]: int(m[2]), m[3]: int(m[4]), m[5]: int(m[6])},
                ),
            )
        ]
    )

    day = au.Day(
        2015,
        16,
        None,
        None,
        part_one,
        part_two,
        input=sue_parser,
        test_input=None,
    )

    day.run_all(run_tests=False)
