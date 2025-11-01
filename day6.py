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
            break

        next_char = board[next_pos]
        if next_char == "#":
            # hit wall → turn right
            icon = turns[icon]
        else:
            # move forward
            pos = next_pos
            visited.add(pos)

    return len(visited)

#PART B
# def obstructed_paths(grid):

#     board, starting_guard_pos, starting_guard_icon = locate_start_position(grid)

#     # movement deltas
#     directions = {
#         "^": (-1, 0),
#         "v": (1, 0),
#         "<": (0, -1),
#         ">": (0, 1)
#     }

#     turns = {  # right turn rule
#         "^": ">",
#         ">": "v",
#         "v": "<",
#         "<": "^"
#     }

#     obstructed_paths = 0
#     for x,y in board:

#         current_tile = board[(x,y)]
#         board_copy, guard_pos, guard_icon = locate_start_position(grid)
#         board_copy[(x,y)] = "*"
#         visited   = set([guard_pos])
#         obstacles = set([guard_pos])


#         if current_tile == ".":
#             obstacles.add((x,y))

#             # Loop guard movement
#             while True:

#                 guard_x, guard_y = guard_pos
#                 guard_dx, guard_dy = directions[guard_icon]
#                 next_guard_pos = (guard_x + guard_dx, guard_y + guard_dy)

#                 if next_guard_pos not in board:
#                     break

#                 if next_guard_pos in visited:
#                     obstructed_paths += 1
#                     break


#                 if next_guard_pos not in obstacles and board_copy[next_guard_pos] == ".":

#                     board_copy[next_guard_pos] = "*"
#                     obstacles.add(next_guard_pos)
#                     visited.add(next_guard_pos)
#                     guard_pos = next_guard_pos

#                 elif next_guard_pos not in obstacles and board_copy[next_guard_pos] != ".":
#                     obstacles.add(next_guard_pos)
#                     visited.add(next_guard_pos)
#                     guard_icon = turns[guard_icon]

#                 elif next_guard_pos in obstacles:
#                     visited.add(next_guard_pos)
#                     guard_icon = turns[guard_icon]
#         else:
#             continue


#     return obstructed_paths


def obstructed_paths(grid):
    board, starting_guard_pos, starting_guard_icon = locate_start_position(grid)

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

    obstructed_paths = 0

    # iterate through all board positions
    for x, y in board:
        current_tile = board[(x, y)]
        if current_tile != ".":  # only try empty spaces
            continue

        # --- FIX 1: shallow copy of board instead of re-locating ---
        board_copy = board.copy()
        guard_pos = starting_guard_pos
        guard_icon = starting_guard_icon

        # --- FIX 2: mark test obstacle as a wall, not "*" ---
        board_copy[(x, y)] = "#"

        visited = set([guard_pos])
        seen_states = set([(guard_pos, guard_icon)])  # track (pos, direction)

        # --- FIX 3: simulate guard movement normally ---
        while True:
            dx, dy = directions[guard_icon]
            gx, gy = guard_pos
            next_pos = (gx + dx, gy + dy)

            # guard exits grid → stop
            if next_pos not in board_copy:
                break

            next_char = board_copy[next_pos]

            if next_char == "#":
                guard_icon = turns[guard_icon]  # turn right
            else:
                guard_pos = next_pos
                visited.add(guard_pos)

            # --- FIX 4: detect loop by state repeat ---
            state = (guard_pos, guard_icon)
            if state in seen_states:
                obstructed_paths += 1
                break
            seen_states.add(state)

    return obstructed_paths

if __name__ == "__main__":
    print(f"PART A: {track_visited_positions(grid)}")
    print(f"PART B: {obstructed_paths(grid)}")
