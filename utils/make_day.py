#!python
import pathlib
import shutil
import os

import click


@click.command()
@click.argument("year", type=int)
@click.argument("day", type=int)
@click.argument(
    "input_data",
    type=click.Path(
        exists=True, dir_okay=False, resolve_path=True, path_type=pathlib.Path
    ),
    default="/mnt/c/Users/micro/Downloads/input.txt",
)
@click.option("-f", "--force", is_flag=True, help="Overwrite existing input")
def make_day(day: int, year: int, input_data: pathlib.Path, force: bool) -> None:
    target = pathlib.Path(".", f"Advent{year}", f"Day{day}")
    os.makedirs(target, exist_ok=True)
    if not force and os.path.isfile(target / "input.txt"):
        print(f"Input data already exists in {target}, ignoring (-f to force)")
    else:
        shutil.copy(input_data, target)

    targetfile = target / f"Day{day}.py"
    print(f"Target is {targetfile}")
    if not os.path.isfile(targetfile):
        shutil.copyfile("utils/template_day.py", targetfile)


if __name__ == "__main__":
    make_day()
