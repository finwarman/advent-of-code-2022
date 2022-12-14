#! /usr/bin/env python3

import re

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

YVALS = [int(x.group(1)) for x in re.finditer(r',(\d+)\b', data)]
XVALS = [int(x.group(1)) for x in re.finditer(r'\b(\d+),', data)]

# ==== SOLUTION ====

FLOOR_Y = max(YVALS) + 2
H = FLOOR_Y

MIN = 0
MAX = max(XVALS) + H
W = abs(MAX - MIN)

grid = [[False for _ in range(W)] for _ in range(H+1)]

for x in range(W):
    grid[FLOOR_Y][x] = True

for row in rows:
    points = row.split(' -> ')
    points = [(int(x)-MIN, int(y)) for x, y in (p.split(',') for p in points)]

    for i in range(len(points)-1):
        x, y = points[i]
        nx, ny = points[i+1]
        itx = 1 if nx >= x else -1
        ity = 1 if ny >= y else -1
        for ly in range(y, ny+ity, ity):
            for lx in range(x, nx+itx, itx):
                grid[ly][lx] = True

SOURCE_X = 500-MIN
sand_count = 0
finished = False
while not finished:
    moving = True
    sand_y = 0
    sand_x = SOURCE_X
    while moving and sand_y < H:
        moving = False
        if not grid[sand_y+1][sand_x]:
            sand_y += 1
            moving = True
        elif not grid[sand_y+1][sand_x-1]:
            sand_y += 1
            sand_x -= 1
            moving = True
        elif not grid[sand_y+1][sand_x+1]:
            sand_y += 1
            sand_x += 1
            moving = True
    if sand_y == 0 and sand_x == 500:
        finished = True
    if sand_y >= H:
        quit(f"voided: error @ x,y ({sand_x}, {sand_y})")
    else:
        grid[sand_y][sand_x] = True
        sand_count += 1

print(sand_count)

# output: 27566
assert sand_count == 27566
