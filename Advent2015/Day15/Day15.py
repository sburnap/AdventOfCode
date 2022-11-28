from dataclasses import dataclass
from typing import Optional

import aoc_utils as au


@dataclass
class Ingred:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def score(
    ingredients: list[Ingred],
    recipe: dict[str, int],
    match_calories: Optional[int] = None,
) -> int:

    # Written for cleanness not speed
    if match_calories and match_calories != sum(
        [ingred.calories * recipe[ingred.name] for ingred in ingredients]
    ):
        return 0

    capacity = max(
        sum([recipe[ingred.name] * ingred.capacity for ingred in ingredients]), 0
    )
    durability = max(
        sum([recipe[ingred.name] * ingred.durability for ingred in ingredients]), 0
    )
    flavor = max(
        sum([recipe[ingred.name] * ingred.flavor for ingred in ingredients]), 0
    )
    texture = max(
        sum([recipe[ingred.name] * ingred.texture for ingred in ingredients]), 0
    )

    return capacity * durability * flavor * texture


# we don't save the recipe because I guess we hate Santa
# We'd need to making a copy of the recipe and return it up the stack
def best_score(
    index: int,
    recipe: dict[str, int],
    ingredients: list[Ingred],
    match_calories: Optional[int] = None,
) -> int:

    to_use = 100 - sum([recipe[ingred.name] for ingred in ingredients[:-1]])

    if index == len(ingredients) - 1 or to_use == 0:
        recipe[ingredients[index].name] = to_use
        return score(ingredients, recipe, match_calories)
    else:
        mx = 0
        for i in range(to_use):
            recipe[ingredients[index].name] = i
            sc = best_score(index + 1, recipe, ingredients, match_calories)
            if sc > mx:
                mx = sc

        return mx


def test_one(ingredients: list[Ingred]) -> int:

    recipe = {ingred.name: 0 for ingred in ingredients}
    return best_score(0, recipe, ingredients)


# expected 18965440
def part_one(ingredients: list[Ingred]) -> int:
    recipe = {ingred.name: 0 for ingred in ingredients}
    return best_score(0, recipe, ingredients)


def test_two(ingredients: list[Ingred]) -> int:

    recipe = {ingred.name: 0 for ingred in ingredients}
    return best_score(0, recipe, ingredients, 500)


# expected 15862900
def part_two(ingredients: list[Ingred]) -> int:
    recipe = {ingred.name: 0 for ingred in ingredients}
    return best_score(0, recipe, ingredients, 500)


if __name__ == "__main__":
    ingred_parser = au.RegexParser(
        [
            (
                "(.*): capacity (.*), durability (.*), flavor (.*), texture (.*), calories (.*)",
                lambda m: Ingred(
                    m[0], int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5])
                ),
            )
        ]
    )

    day = au.Day(
        2015,
        15,
        test_one,
        test_two,
        part_one,
        part_two,
        input=ingred_parser,
        test_input=ingred_parser,
    )

    day.run_all(run_tests=True)
