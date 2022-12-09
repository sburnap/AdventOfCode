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
    head = Location(0, 0)
    tail = Location(0, 0)

    rope = [Location(0, 0)] * length

    visited: set[str] = set()

    for move in moves:
        for _ in range(move.distance):
            match move.direction:
                case "U":
                    head.y -= 1
                case "D":
                    head.y += 1
                case "L":
                    head.x -= 1
                case "R":
                    head.x += 1

            diffy = head.y - tail.y
            diffx = head.x - tail.x
            if abs(diffy) >= 2 and abs(diffx) == 0:
                tail.y += diffy // abs(diffy)
            elif abs(diffx) >= 2 and abs(diffy) == 0:
                tail.x += diffx // abs(diffx)
            elif abs(diffy) >= 2 or abs(diffx) >= 2:
                tail.y += diffy // abs(diffy)
                tail.x += diffx // abs(diffx)

            visited.add(f"{tail.x},{tail.y}")

    return len(visited)


def test_one(moves: list[Move]) -> Optional[int]:
    return do_moves(moves)


def part_one(moves: list[str]) -> Optional[int]:
    return do_moves(moves)


def test_two(input: str) -> Optional[int]:
    return None


def part_two(input: list[str]) -> Optional[int]:
    return None


if __name__ == "__main__":
    move_parser = au.RegexParser(
        [("^(D|U|R|L) (\d*)$", lambda m: Move(m[0], int(m[1])))]
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
