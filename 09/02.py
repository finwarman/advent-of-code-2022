#! /usr/bin/env python3

from math import copysign

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip().split(' ') for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

head = (0, 0)
knots = [(0, 0) for _ in range(9)]

tail_positions = set()
tail_positions.add((0,0))

dir_steps = {
    'R': ( 1,  0),
    'U': ( 0,  1),
    'L': (-1,  0),
    'D': ( 0, -1),
}

def follow_head(knot, head):
    kx, ky = knot
    hx, hy = head
    # adjacent
    if abs(kx-hx) <= 1 and abs(ky-hy) <= 1:
        return knot
    # up/down
    if kx == hx and abs(ky-hy)==2:
        return kx, ky + int(copysign(1, hy-ky))
    # left/right
    if ky == hy and abs(kx-hx)==2:
        return kx + int(copysign(1, hx-kx)), ky
    # diagonal
    return kx + int(copysign(1, hx-kx)), ky + int(copysign(1, hy-ky))

for direction, steps in rows:
    steps = int(steps)
    head_dx, head_dy = dir_steps[direction]

    for i in range(steps):
        head = (head[0]+head_dx, head[1]+head_dy)
        prev_x, prev_y = head

        for j, knot in enumerate(knots):
            knots[j] = follow_head(knot, (prev_x, prev_y))
            prev_x, prev_y = knots[j]

        tail_positions.add(knots[-1])

result = len(tail_positions)
print(result)

# output: 2445
assert result == 2445
