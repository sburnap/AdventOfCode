from typing import Optional
from dataclasses import dataclass

import aoc_utils as au


@dataclass
class Move:
    direction: str
    distance: int


@dataclass
class Location:
    x: int
    y: int

    def __repr__(self) -> str:
        return f"{self.x},{self.y}"


def do_moves(moves: list[Move], length: int = 2) -> int:
    visited: set[str] = set()
    rope = [Location(0, 0) for _ in range(length)]

    for move in moves:
        for _ in range(move.distance):
            match move.direction:
                case "U":
                    rope[0].y -= 1
                case "D":
                    rope[0].y += 1
                case "L":
                    rope[0].x -= 1
                case "R":
                    rope[0].x += 1

            for i in range(len(rope) - 1):
                diffy = rope[i].y - rope[i + 1].y
                diffx = rope[i].x - rope[i + 1].x

                if abs(diffy) > 1 or abs(diffx) > 1:
                    if abs(diffy) > 0:
                        rope[i + 1].y += diffy // abs(diffy)
                    if abs(diffx) > 0:
                        rope[i + 1].x += diffx // abs(diffx)

            visited.add(f"{rope[-1].x},{rope[-1].y}")

    return len(visited)


def test_one(moves: list[Move]) -> Optional[int]:
    return do_moves(moves)


# expected 6464
def part_one(moves: list[Move]) -> Optional[int]:
    return do_moves(moves)


def test_two(moves: list[Move]) -> Optional[int]:
    return do_moves(moves, 10)


# expect 2604
def part_two(moves: list[Move]) -> Optional[int]:
    return do_moves(moves, 10)


if __name__ == "__main__":
    move_parser = au.RegexParser(
        [(r"^(D|U|R|L) (\d*)$", lambda m: Move(m[0], int(m[1])))]
    )
    day = au.Day(
        2022,
        9,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=move_parser,
        input=move_parser,
    )

    day.run_all(run_tests=True)
