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

signal_sum = 0

for row in rows:
    clock += 1
    if clock == 20 or (clock > 20 and ((clock - 20)) % 40 == 0):
        signal_sum += (clock * reg_x)

    if row[0:3] == 'add':
        arg = int(row.split(' ')[1])

        clock += 1
        if clock == 20 or (clock > 20 and ((clock - 20)) % 40 == 0):
            signal_sum += (clock * reg_x)

        reg_x += arg

print(signal_sum)

# output: 14420
assert signal_sum == 14420
