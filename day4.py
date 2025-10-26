import re
import os

here = os.path.dirname(__file__)
input_path = os.path.join(here, "day4input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

def parse_3x3_optimal(grid:list[str]) -> int:
    nrows, ncols = len(lines), len(lines[0])
    count = 0
    for x in range(1, nrows - 1):
        for y in range(1, ncols - 1):
            if grid[x][y] != "A":
                continue

            left_diag = grid[x-1][y-1] + grid[x][y] + grid[x+1][y+1]
            right_diag = grid[x-1][y+1] + grid[x][y] + grid[x+1][y-1]
            if left_diag in ("MAS", "SAM") and right_diag in ("MAS", "SAM"):
                count += 1

    return count

def is_valid_3x3_MM(grid:list[str], start_x, start_y):
    if start_x <= len(grid) - 3:
        if start_y <= len(grid[0]) - 3:
            if grid[start_x+2][start_y] == "S":
                if grid[start_x+2][start_y+2] == "S":
                   if grid[start_x+1][start_y+1] == "A":
                        return True
    return False

def is_valid_3x3_SM(grid:list[str], start_x, start_y):
    if start_x <= len(grid) - 3:
        if start_y <= len(grid[0]) - 3:
            if grid[start_x+2][start_y] == "S":
                if grid[start_x+2][start_y+2] == "M":
                   if grid[start_x+1][start_y+1] == "A":
                        return True
    return False

def is_valid_3x3_MS(grid:list[str], start_x, start_y):
    if start_x <= len(grid) - 3:
        if start_y <= len(grid[0]) - 3:
            if grid[start_x+2][start_y] == "M":
                if grid[start_x+2][start_y+2] == "S":
                   if grid[start_x+1][start_y+1] == "A":
                        return True
    return False

def is_valid_3x3_SS(grid:list[str], start_x, start_y):
    if start_x <= len(grid) - 3:
        if start_y <= len(grid[0]) - 3:
            if grid[start_x+2][start_y] == "M":
                if grid[start_x+2][start_y+2] == "M":
                   if grid[start_x+1][start_y+1] == "A":
                        return True
    return False

def parse_xmas3x3(lines: list[str]) -> int:
    nrows, ncols = len(lines), len(lines[0])
    # Rows and columns
    rows = lines
    cols = [''.join(col) for col in zip(*lines)]
    count = 0

    for x, row in enumerate(rows):
        if re.search(r"M.S|S.M|M.M|S.S", row):
            for y in range(ncols):
                if y+2 <= len(row) - 1:
                    if lines[x][y] == "M" and lines[x][y+2] == "S":
                        if is_valid_3x3_MS(lines, x, y):
                            count += 1

                    if lines[x][y] == "S" and lines[x][y+2] == "S":
                        if is_valid_3x3_SS(lines, x, y):
                            count += 1

                    if lines[x][y] == "M" and lines[x][y+2] == "M":
                        if is_valid_3x3_MM(lines, x, y):
                            count += 1

                    if lines[x][y] == "S" and lines[x][y+2] == "M":
                        if is_valid_3x3_SM(lines, x, y):
                            count += 1
    return count


def parse_xmas(lines: list[str]) -> None:
    nrows, ncols = len(lines), len(lines[0])

    # Rows and columns
    rows = lines
    cols = [''.join(col) for col in zip(*lines)]

    # Top-left → bottom-right (\)
    diag1 = [
        ''.join(lines[r + k][c + k] for k in range(min(nrows - r, ncols - c)))
        for r in range(nrows) for c in range(ncols)
        if r == 0 or c == 0
    ]

    # Top-right → bottom-left (/)
    diag2 = [
        ''.join(lines[r + k][c - k] for k in range(min(nrows - r, c + 1)))
        for r in range(nrows) for c in range(ncols)
        if r == 0 or c == ncols - 1
    ]

    return sum(s.count("XMAS") + s.count("SAMX") for s in rows + cols + diag1 + diag2)




if __name__ == "__main__":
    print ("===Day 4===")
    print(f"PART A: {parse_xmas(lines)}")
    print(f"PART B: {parse_xmas3x3(lines)}")
    print(f"PART B Optimal: {parse_3x3_optimal(lines)}")