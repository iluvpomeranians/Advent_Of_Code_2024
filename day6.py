import os
import re

here = os.path.dirname(__file__)
input_path = os.path.join(here, "day6input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    grid = [line.strip() for line in f if line.strip()]


def locate_start_position(grid):
    icon_patterns = r"[<>^v]"
    board = {}
    start = None
    icon = None

    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            board[(x, y)] = char
            if re.search(icon_patterns, char):
                start = (x, y)
                icon = char
                print(f"Starting {char} at ({x}, {y})")

    return board, start, icon


def track_visited_positions(grid):
    board, pos, icon = locate_start_position(grid)
    visited = set([pos])

    # movement deltas
    directions = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1)
    }

    turns = {  # right turn rule
        "^": ">",
        ">": "v",
        "v": "<",
        "<": "^"
    }

    while True:
        dx, dy = directions[icon]
        x, y = pos
        next_pos = (x + dx, y + dy)

        # If we’re outside the board
        if next_pos not in board:
            print("Outside board — stopping.")
            break

        next_char = board[next_pos]
        if next_char == "#":
            # hit wall → turn right
            icon = turns[icon]
        else:
            # move forward
            pos = next_pos
            visited.add(pos)

    print(f"Visited {len(visited)} unique tiles.")
    return len(visited)


if __name__ == "__main__":
    print(f"PART A: {track_visited_positions(grid)}")
