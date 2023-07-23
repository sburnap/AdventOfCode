from typing import Optional, Generator
from dataclasses import dataclass

import aoc_utils as au


@dataclass
class Position:
    x: int
    y: int

    def offset(self, p: "Position") -> "Position":
        return Position(self.x + p.x, self.y + p.y)

    def __hash__(self):
        return hash(f"{self.x},{self.y}")

    def __str__(self):
        return f"[{self.x},{self.y}]"


class Block:
    def __init__(self, position: Position):
        self.position = position
        self.shape: list[Position] = []

    def __repr__(self):
        return f"{self.__class__} : {self.position}"

    def move(self, offset: Position) -> None:

        self.position = self.position.offset(offset)

    def covers(self) -> set[Position]:
        return set([position.offset(self.position) for position in self.shape])

    def can_drop(self, filled_spots: set[Position]) -> bool:
        potential = set(position.offset(Position(0, -1)) for position in self.covers())

        return len(filled_spots.intersection(potential)) == 0

    def can_left(self, filled_spots: set[Position]) -> bool:
        if all(position.x + self.position.x > 0 for position in self.shape):

            potential = set(
                position.offset(Position(-1, 0)) for position in self.covers()
            )

            return len(filled_spots.intersection(potential)) == 0
        else:
            return False

    def can_right(self, filled_spots: set[Position]) -> bool:
        if all(position.x + self.position.x < 6 for position in self.shape):

            potential = set(
                position.offset(Position(1, 0)) for position in self.covers()
            )

            return len(filled_spots.intersection(potential)) == 0
        else:
            return False


class Line(Block):
    def __init__(self, position: Position):
        super().__init__(position)
        self.shape = [
            Position(0, 0),
            Position(1, 0),
            Position(2, 0),
            Position(3, 0),
        ]


class Plus(Block):
    def __init__(self, position: Position):
        super().__init__(position)
        self.shape = [
            Position(1, 2),
            Position(0, 1),
            Position(1, 1),
            Position(2, 1),
            Position(1, 0),
        ]


class BackwardsL(Block):
    def __init__(self, position: Position):
        super().__init__(position)
        self.shape = [
            Position(2, 2),
            Position(2, 1),
            Position(0, 0),
            Position(1, 0),
            Position(2, 0),
        ]


class Pole(Block):
    def __init__(self, position: Position):
        super().__init__(position)
        self.shape = [
            Position(0, 3),
            Position(0, 2),
            Position(0, 1),
            Position(0, 0),
        ]


class Square(Block):
    def __init__(self, position: Position):
        super().__init__(position)
        self.shape = [
            Position(0, 1),
            Position(1, 1),
            Position(0, 0),
            Position(1, 0),
        ]


def blockgen() -> Generator[type, None, None]:
    while True:
        yield Line
        yield Plus
        yield BackwardsL
        yield Pole
        yield Square


def jetgen(jets: str) -> Generator[str, None, None]:
    while True:
        for ch in jets:
            yield ch


def draw(filled_spots: set[Position]) -> None:

    top = max(position.y for position in filled_spots)
    bottom = min(position.y for position in filled_spots)

    for y in range(top + 3, bottom - 1, -1):
        print(
            "".join(
                [f"{y:03}", "|"]
                + ["#" if Position(x, y) in filled_spots else "." for x in range(7)]
                + ["|"]
            )
        )
    print("+-------+")


def drop_test(input: str, count: int) -> int:

    last = 0
    lastdiff = 0
    jets = jetgen(input)

    filled_spots: set[Position] = set(Position(x, -1) for x in range(7))
    for dropped, btype in enumerate(blockgen()):
        entry = Position(2, 4 + max(position.y for position in filled_spots))
        b: Block = btype(entry)

        while True:
            match next(jets):
                case "<":
                    if b.can_left(filled_spots):
                        b.move(Position(-1, 0))
                case ">":
                    if b.can_right(filled_spots):
                        b.move(Position(1, 0))

            if not b.can_drop(filled_spots):
                break

            b.move(Position(0, -1))
            # print("FALL", b)

        for position in b.covers():
            filled_spots.add(position)

        top = max(position.y for position in filled_spots) + 1

        if dropped % 50455 == 50454:
            # if dropped % 200 == 199:
            print(f"{top-last}")
            lastdiff = top - last
            last = top

        if dropped == count - 1:
            # draw(filled_spots)
            return top

        empty = set(range(7))

        while len(empty) > 0 and top > top - 4:
            for x in list(empty):
                if Position(x, top) in filled_spots:
                    empty.discard(x)
            top -= 1

        if top > 0:
            filled_spots = set(
                position for position in filled_spots if position.y >= top
            )

    raise Exception("infinite generator exhausted, oh my")


def test_one(input: str) -> Optional[int]:

    print(len(input) * 5)
    return drop_test(input, 2022)


def part_one(input: str) -> Optional[int]:
    print(len(input) * 5)
    return None
    return drop_test(input, 2022)


def test_two(input: str) -> Optional[int]:
    return drop_test(input, 100 * len(input) * 5)


def part_two(input: str) -> Optional[int]:
    return drop_test(input, 200 * len(input) * 5)


if __name__ == "__main__":
    day = au.Day(
        2022,
        17,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=au.OneLineParser(),
        input=au.OneLineParser(),
    )

    day.run_all(run_tests=True)
