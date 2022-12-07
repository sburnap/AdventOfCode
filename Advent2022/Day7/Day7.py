from typing import Optional, Any
from dataclasses import dataclass
from itertools import combinations

import aoc_utils as au


@dataclass
class ChangeDirCmd:
    target: str


@dataclass
class ListDir:
    pass


@dataclass
class DirEntry:
    name: str


@dataclass
class FileEntry:
    size: int
    name: str


def make_path(cwd: list[str], name: str) -> str:
    return "/".join(cwd) + "/" + name


def get_dirs(
    shell_stuff: list[ChangeDirCmd | ListDir | DirEntry | FileEntry],
) -> dict[str, int]:

    dirs = {"/": 0}
    cwd = ["/"]

    for shell_item in shell_stuff:
        match shell_item:
            case ChangeDirCmd() as cd_cmd:
                match cd_cmd.target:
                    case "/":
                        cwd = ["/"]
                    case "..":
                        if len(cwd) > 1:
                            cwd.pop()
                        else:
                            raise Exception("Tried to go above root")
                    case _:
                        cwd.append(make_path(cwd, cd_cmd.target))
            case ListDir():
                pass
            case DirEntry() as dir_entry:
                if (fullpath := make_path(cwd, dir_entry.name)) not in dirs:
                    dirs[fullpath] = 0
            case FileEntry() as file_entry:
                for dir in cwd:
                    dirs[dir] += file_entry.size
            case _:
                raise (f"Unknown object {shell_item} seen")
    return dirs


def find_space(shell_stuff: list[ChangeDirCmd | ListDir | DirEntry | FileEntry]) -> int:

    dirs = get_dirs(shell_stuff)
    return sum([dir for dir in dirs.values() if dir <= 100000])


def find_space2(
    shell_stuff: list[ChangeDirCmd | ListDir | DirEntry | FileEntry],
) -> int:

    dirs = get_dirs(shell_stuff)

    needed = 30000000 - (70000000 - dirs["/"])

    return min([dir for dir in dirs.values() if dir >= needed])


def test_one(
    shell_stuff: list[ChangeDirCmd | ListDir | DirEntry | FileEntry],
) -> Optional[int]:
    return find_space(shell_stuff)


# expected 1348005
def part_one(
    shell_stuff: list[ChangeDirCmd | ListDir | DirEntry | FileEntry],
) -> Optional[int]:
    return find_space(shell_stuff)


def test_two(
    shell_stuff: list[ChangeDirCmd | ListDir | DirEntry | FileEntry],
) -> Optional[int]:
    return find_space2(shell_stuff)


# expected 12785886
def part_two(
    shell_stuff: list[ChangeDirCmd | ListDir | DirEntry | FileEntry],
) -> Optional[int]:
    return find_space2(shell_stuff)


if __name__ == "__main__":
    shell_parser = au.RegexParser(
        [
            (r"\$ cd (.*)", lambda m: ChangeDirCmd(m[0])),
            (r"\$ ls", lambda m: ListDir()),
            (r"dir (.*)", lambda m: DirEntry(m[0])),
            (r"(\d*) (.*)", lambda m: FileEntry(int(m[0]), m[1])),
        ]
    )
    day = au.Day(
        2022,
        7,
        test_one,
        test_two,
        part_one,
        part_two,
        test_input=shell_parser,
        input=shell_parser,
    )

    day.run_all(run_tests=True)
