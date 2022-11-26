import aoc_utils as au


def count_characters_decode(input: str) -> int:

    i = 0
    cnt = 0
    while i < len(input):
        match input[i]:
            case '"':
                pass
            case "\\":
                i += 1
                match input[i]:
                    case "x":
                        cnt += 1
                        i += 2
                    case '"' | "\\":
                        cnt += 1
                    case _:
                        raise Exception(f"Bad character encountered \\{input[i]}")
            case _:
                cnt += 1
        i += 1
    return cnt


def test_one(input: str) -> int:
    return count_characters_decode(input)


def part_one(input: list[str]) -> int:
    return sum([len(line) - count_characters_decode(line) for line in input])


def count_characters_encode(input: str) -> int:

    return sum([2 if ch in ['"', "\\"] else 1 for ch in input]) + 2


def test_two(input: str) -> int:
    return count_characters_encode(input)


def part_two(input: list[str]) -> int:
    return sum([count_characters_encode(line) - len(line) for line in input])


if __name__ == "__main__":
    day = au.Day(
        2015,
        8,
        test_one,
        test_two,
        part_one,
        part_two,
        input=au.Day.InType.INPUT_MULTI_LINE_STR,
        test_input=['""', '"abc"', '"aaa\\"aaa"', '"\\x27"'],
    )

    day.run_all(run_tests=True)
