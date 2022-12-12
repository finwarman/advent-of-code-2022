#! /usr/bin/env python3
import re
import math

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

head = (0, 0)
tail = (0, 0)

tail_positions = set([tail])

dir_steps = {
    'R': ( 1,  0),
    'U': ( 0,  1),
    'L': (-1,  0),
    'D': ( 0, -1),
}

for row in rows:
    direction, steps = row.split(' ')
    steps = int(steps)

    dhx, dhy = dir_steps[direction]
    for i in range(steps):
        head = x, y = head[0]+dhx, head[1]+dhy

        tx, ty = tail
        dx, dy = x - tx, y - ty
        if abs(dx) > 1 or abs(dy) > 1:
            tail = (tx + (dx - dhx), ty + (dy - dhy))

        tail_positions.add(tail)


result = len(tail_positions)
print(result)

# output: 5902
assert result == 5902
