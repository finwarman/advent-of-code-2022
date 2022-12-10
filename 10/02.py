#! /usr/bin/env python3
import re
import math

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

clock = 0
reg_x = 1

crt_rows = []

WIDTH, HEIGHT = 40, 6
LO, HI = ' ', '█'

def update_sprite(x):
    row = [LO for _ in range(WIDTH)]
    for pos in [x-1, x, x+1]:
        if pos >= 0 and pos < WIDTH:
            row[pos] = HI
    return row

sprite_row = update_sprite(reg_x)

for row in rows:
    crt_rows.append(sprite_row[clock % WIDTH])
    clock += 1

    if row[0:3] == 'add':
        arg = int(row.split(' ')[1])

        crt_rows.append(sprite_row[clock % WIDTH])
        clock += 1

        reg_x += arg
        sprite_row = update_sprite(reg_x)

for i in range(HEIGHT):
    for j in range(WIDTH):
        print(crt_rows[WIDTH * i + j], end='')
    print()

# output: RGLRBZAU
# ███   ██  █    ███  ███  ████  ██  █  █
# █  █ █  █ █    █  █ █  █    █ █  █ █  █
# █  █ █    █    █  █ ███    █  █  █ █  █
# ███  █ ██ █    ███  █  █  █   ████ █  █
# █ █  █  █ █    █ █  █  █ █    █  █ █  █
# █  █  ███ ████ █  █ ███  ████ █  █  ██
