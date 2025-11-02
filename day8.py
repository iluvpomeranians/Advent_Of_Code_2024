import os
import re
import itertools
from pprint import pprint

here = os.path.dirname(__file__)
input_path = os.path.join(here, "day8input.txt")

with open(input_path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

gridSet = set()
gridDict = {}
def createMap():
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            gridSet.add((char, x, y))
            if char != ".":
                gridDict.setdefault(char, []).append((x,y))

    return detectAntiNodes(gridDict)

def printGrid(gridLUT):
    max_x = max(x for x, _ in gridLUT)
    max_y = max(y for _, y in gridLUT)
    for x in range(max_x + 1):
        line = ''.join(gridLUT.get((x, y), '.') for y in range(max_y + 1))
        print(line)


seen = set()
gridLUTCOPY = None
def detectAntiNodes(gridDict):
    antinodes = 0
    gridLUT = {(x, y): ch for (ch, x, y) in gridSet}

    for key, val in gridDict.items():
        for coord in val:
            x1,y1 = coord
            node_matches = [(char, a, b) for (char , a, b) in gridSet if (char) == (key) and (x1,y1) != (a,b)]
            for node in node_matches:
                (_, x2, y2) = node

                checkDiagonals((x1,y1), (x2,y2), gridLUT, seen)

    #printGrid(gridLUT)
    for node in gridLUT:
        if gridLUT.get(node) != ".":
            antinodes += 1
    return antinodes

def checkDiagonals(coord1: tuple, coord2: tuple, gridLUT: dict, seen : set):
    antiNodes = 0
    x1, y1 = coord1
    x2, y2 = coord2

    dx, dy = x2 - x1, y2 - y1
    a = (x2 + dx, y2 + dy)
    b = (x1 - dx, y1 - dy)

    #Keep creating new positions as long as they exist in the grid
    while a in gridLUT or b in gridLUT:
        for node in (a, b):
            if node in gridLUT and node not in seen:
                seen.add(node)
                if gridLUT[node] == ".":
                    gridLUT[node] = "#"
                antiNodes += 1

        a = (a[0] + dx, a[1] + dy)
        b = (b[0] - dx, b[1] - dy)

    return antiNodes


if __name__ == "__main__":
    print(f"PART B: {createMap()}")



