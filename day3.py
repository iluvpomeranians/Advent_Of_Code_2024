import re
import os

here = os.path.dirname(__file__)
input_path = os.path.join(here, "day3input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

def parse_muls(lines: list):
    total = 0
    enabled = True

    for line in lines:
        for token in re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", line):
            if token == "do()":
                enabled = True
            elif token == "don't()":
                enabled = False
            elif enabled:
                for a, b in re.findall(r"\((\d+),(\d+)\)", token):
                    total += int(a) * int(b)

    return total


if __name__ == "__main__":
    print(parse_muls(lines))