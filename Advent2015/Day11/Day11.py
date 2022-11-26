import aoc_utils as au


valid = "abcdefghjkmnopqrstuvwxyz"


def increment(password: str):

    carry = True
    out = ""
    for ch in password[::-1]:
        if carry:
            if ch != "z":
                out += chr(ord(ch) + 1)
                carry = False
            else:
                out += "a"
        else:
            out += ch

    return out[::-1]


def valid(password: str):
    if set(["i", "l", "o"]).intersection(set(password)):
        return False

    saw_straight = False
    saw_pairs = False
    pairs = []
    for i in range(len(password) - 1):
        if (
            i < len(password) - 2
            and ord(password[i]) == ord(password[i + 1]) - 1
            and ord(password[i]) == ord(password[i + 2]) - 2
        ):
            saw_straight = True

        if password[i] == password[i + 1] and password[i : i + 2] not in pairs:
            pairs.append(password[i : i + 2])
            if len(pairs) >= 2:
                saw_pairs = True

        if saw_straight and saw_pairs:
            return True

    return False


def test_one(input: str) -> int:

    nextp = increment(input)

    while not valid(nextp):
        nextp = increment(nextp)

    return f"{valid(input)}, {nextp}"


def part_one(input: list[str]) -> int:
    nextp = increment(input)

    while not valid(nextp):
        nextp = increment(nextp)

    return nextp


def part_two(input: list[str]) -> int:

    nextp = input
    for i in range(2):
        nextp = increment(nextp)

        while not valid(nextp):
            nextp = increment(nextp)

    return nextp


if __name__ == "__main__":
    day = au.Day(
        2015,
        11,
        test_one,
        None,
        part_one,
        part_two,
        input="hepxcrrq",
        test_input=[
            "ghjaabcb",
            # "hijklmmn",
            "abbceffg",
            "abbcegjk",
            "abcdefgh",
            # "ghijklmn",
            "abcdffaa",
            "ghjaabcc",
        ],
    )

    day.run_all(run_tests=True)
