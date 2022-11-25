import aoc_utils as au
import hashlib


def make_hash(n: int, input: str) -> str:
    m = hashlib.md5()
    m.update(str.encode(f"{input}{n}"))
    return m.hexdigest()


def find_hash_num(input: str, num_zeroes: int) -> int:
    n = 1
    while (hash := make_hash(n, input))[:num_zeroes] != "0" * num_zeroes:
        n += 1
    return n


def test_one(test_input: str) -> int:
    return find_hash_num(test_input, 5)


def part_one(input: str) -> int:
    return find_hash_num(input, 5)


def test_two(test_input: str) -> int:
    return find_hash_num(test_input, 6)


def part_two(input: str) -> int:
    return find_hash_num(input, 6)


if __name__ == "__main__":
    day = au.Day(
        2015,
        4,
        test_one,
        test_two,
        part_one,
        part_two,
        input="ckczppom",
        test_input=["abcdef", "pqrstuv"],
    )

    day.run_all(run_tests=True)
