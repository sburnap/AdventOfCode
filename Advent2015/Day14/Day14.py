import aoc_utils as au


class Deer:
    def __init__(self, name: str, speed: int, travel: int, rest: int):
        self.name = name
        self.speed = speed
        self.travel = travel
        self.rest = rest
        self.position = 0
        self.score = 0

    def distance(self, seconds: int) -> int:

        num_segments = seconds // (self.travel + self.rest)
        partial = seconds - (self.travel + self.rest) * num_segments

        total = (
            num_segments * self.travel * self.speed
            + min(partial, self.travel) * self.speed
        )
        return total

    def cycle(self, time_step: int) -> None:
        place_in_cycle = time_step % (self.travel + self.rest)
        if place_in_cycle < self.travel:
            self.position += self.speed

    def __repr__(self):
        return f"{self.name} speed {self.speed} travel {self.travel} rest {self.rest}"


# clear naming trumps grammar
def test_one(deers: list[Deer]) -> int:
    return max([deer.distance(1000) for deer in deers])


# expected 2696
def part_one(deers: list[Deer]) -> int:
    return max([deer.distance(2503) for deer in deers])


def run_race(deers: list[Deer], seconds: int) -> int:
    for time_step in range(seconds):

        for deer in deers:
            deer.cycle(time_step)

        max_position = max(deer.position for deer in deers)
        for deer in deers:
            if deer.position == max_position:
                deer.score += 1

    return max([deer for deer in deers], key=lambda d: d.score).score


def test_two(deers: list[Deer]) -> int:
    return run_race(deers, 1000)


# expected 1084
def part_two(deers: list[Deer]) -> int:
    return run_race(deers, 2503)


if __name__ == "__main__":
    deer_parser = au.RegexParser(
        [
            (
                "(.*) can fly (\d*) km/s for (\d*) seconds, but then must rest for (\d*) seconds.",
                lambda m: Deer(m[0], int(m[1]), int(m[2]), int(m[3])),
            )
        ]
    )
    day = au.Day(
        2015,
        14,
        test_one,
        test_two,
        part_one,
        part_two,
        input=deer_parser,
        test_input=deer_parser,
    )

    day.run_all(run_tests=True)
