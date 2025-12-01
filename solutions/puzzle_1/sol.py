import csv
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data.txt"
START = 50


def read_data(filepath: Path) -> list[str]:
    data = []
    with open(filepath) as file:
        for row in csv.reader(file):
            data.append(row[0])
    return data


def break_safe(instructions: list[str]) -> int:
    counter = 0
    cur = START

    for i in instructions:
        side = i[0]
        num = int(i[1:])

        if num == 0:
            continue

        match side:
            case 'L':
                cur -= 1
                counter += cur // 100 - (cur - num) // 100
                cur += 1
                cur -= num
            case 'R':
                counter += (cur + num) // 100 - cur // 100
                cur += num

    return counter


if __name__ == "__main__":
    data = read_data(DATA_PATH)
    print(break_safe(data))
