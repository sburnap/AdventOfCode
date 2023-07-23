from typing import Optional
from dataclasses import dataclass

import aoc_utils as au


@dataclass
class Robots:
    ore: int
    clay: int
    obsidian: int
    geode: int


@dataclass
class Materials:
    ore: int
    clay: int
    obsidian: int
    geode: int

    def __add__(self, other: "Materials"):
        return Materials(
            self.ore + other.ore,
            self.clay + other.clay,
            self.obsidian + other.obsidian,
            self.geode + other.geode,
        )


@dataclass
class Blueprint:
    number: int
    ore_for_ore: int
    ore_for_clay: int
    ore_for_obsidian: int
    clay_for_obsidian: int
    ore_for_geode: int
    obsidian_for_geode: int

    def evaluate2(self) -> Optional[int]:
        robots = Robots(1, 0, 0, 0)
        stockpile = Materials(0, 0, 0, 0)

        obsidian_ratio = self.obsidian_for_geode / self.ore_for_geode
        clay_ore_ratio = self.clay_for_obsidian / self.ore_for_obsidian

        for timeleft in range(24):
            new_materials = Materials(
                robots.ore, robots.clay, robots.obsidian, robots.geode
            )

            if (
                stockpile.ore >= self.ore_for_geode
                and stockpile.obsidian >= self.obsidian_for_geode
            ):
                plan = "G"

            elif (
                stockpile.ore
                and obsidian_ratio - (stockpile.obsidian / stockpile.ore) > 1.5
                and stockpile.ore >= self.ore_for_obsidian
                and stockpile.clay >= self.clay_for_obsidian
            ):
                plan = "B"
            elif (
                stockpile.ore
                and clay_ore_ratio - (stockpile.clay / stockpile.ore) > 1.5
                and stockpile.ore >= self.ore_for_clay
            ):
                plan = "C"
            elif stockpile.ore >= self.ore_for_ore:
                plan = "O"
            else:
                plan = "_"

            match plan:
                case "O":
                    stockpile.ore -= self.ore_for_ore
                    robots.ore += 1
                case "C":
                    stockpile.ore -= self.ore_for_clay
                    robots.clay += 1
                case "B":
                    stockpile.ore -= self.ore_for_obsidian
                    stockpile.clay -= self.clay_for_obsidian
                    robots.obsidian += 1
                case "G":
                    stockpile.ore -= self.ore_for_geode
                    stockpile.obsidian -= self.obsidian_for_geode
                    robots.geode += 1

            stockpile += new_materials
            print("-")
        return stockpile.geode

    def evaluate(self) -> Optional[int]:
        robots = Robots(1, 0, 0, 0)
        stockpile = Materials(0, 0, 0, 0)

        obsidian_ratio = self.obsidian_for_geode / self.ore_for_geode
        clay_ore_ratio = self.clay_for_obsidian / self.ore_for_obsidian

        for timeleft in range(24):
            new_materials = Materials(
                robots.ore, robots.clay, robots.obsidian, robots.geode
            )

            projected_ore = (23 - timeleft) * robots.ore + stockpile.ore
            projected_clay = (23 - timeleft) * robots.clay + stockpile.clay
            projected_obsidian = (23 - timeleft) * robots.obsidian + stockpile.obsidian
            projected_geode = (24 - timeleft) * robots.geode + stockpile.geode
            if (
                projected_clay / projected_ore - clay_ore_ratio < 1.5
                or projected_obsidian / projected_ore - obsidian_ratio < 1.5
            ):
                if (
                    projected_clay / projected_ore - clay_ore_ratio
                    > projected_obsidian / projected_ore - obsidian_ratio
                ):
                    need_clay = False
                    need_obsidian = True
                else:
                    need_clay = True
                    need_obsidian = False

            if (
                stockpile.ore >= self.ore_for_geode
                and stockpile.obsidian >= self.obsidian_for_geode
            ):
                plan = "G"
            elif (
                need_obsidian
                and stockpile.ore >= self.ore_for_obsidian
                and stockpile.clay >= self.clay_for_obsidian
            ):
                plan = "B"
            elif need_clay and stockpile.ore >= self.ore_for_clay:
                plan = "C"
            elif stockpile.ore >= self.ore_for_ore:
                plan = "O"
            else:
                plan = "_"

            match plan:
                case "O":
                    stockpile.ore -= self.ore_for_ore
                    robots.ore += 1
                case "C":
                    stockpile.ore -= self.ore_for_clay
                    robots.clay += 1
                case "B":
                    stockpile.ore -= self.ore_for_obsidian
                    stockpile.clay -= self.clay_for_obsidian
                    robots.obsidian += 1
                case "G":
                    stockpile.ore -= self.ore_for_geode
                    stockpile.obsidian -= self.obsidian_for_geode
                    robots.geode += 1

            stockpile += new_materials
            print("-")
        return stockpile.geode


def test_one(blueprints: list[Blueprint]) -> Optional[int]:
    for blueprint in blueprints:
        print(blueprint.evaluate())
    return None


def part_one(blueprints: list[Blueprint]) -> Optional[int]:
    return None
    for blueprint in blueprints:
        print(blueprint.evaluate())
    return None


def test_two(input: str) -> Optional[int]:
    return None


def part_two(input: list[str]) -> Optional[int]:
    return None


if __name__ == "__main__":
    blueprint_parser = au.RegexParser(
        [
            (
                r"^Blueprint (\d*): Each ore robot costs (\d*) ore. "
                r"Each clay robot costs (\d*) ore. "
                r"Each obsidian robot costs (\d*) ore and (\d*) clay. "
                r"Each geode robot costs (\d*) ore and (\d*) obsidian.$",
                lambda m: Blueprint(
                    int(m[0]),
                    int(m[1]),
                    int(m[2]),
                    int(m[3]),
                    int(m[4]),
                    int(m[5]),
                    int(m[6]),
                ),
            ),
        ]
    )
    day = au.Day(
        2022,
        19,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=blueprint_parser,
        input=blueprint_parser,
    )

    day.run_all(run_tests=True)
