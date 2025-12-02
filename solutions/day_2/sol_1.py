
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data.txt"


def read_data(filepath: Path) -> list[str]:
    with open(filepath) as file:
        lines = file.readlines()
    return lines[0].split(",")


def is_repetition(s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    mid = len(s) // 2
    return s[:mid] == s[mid:]


def is_repetition_2(s: str) -> bool:
    return s in (s + s)[1:-1]


def solve(data: list[int]) -> int:

    res = 0

    for i in data:
        first, second = i.split("-")

        for j in range(int(first), int(second)+1):
            if is_repetition(str(j)):
                res += j
    return res


def solve_2(data: list[int]) -> int:

    res = 0

    for i in data:
        first, second = i.split("-")

        for j in range(int(first), int(second)+1):
            if is_repetition_2(str(j)):
                res += j
    return res


if __name__ == "__main__":
    data = read_data(DATA_PATH)
    print(solve(data))
    print(solve_2(data))
