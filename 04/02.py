#! /usr/bin/env python3

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

total = 0

for row in rows:
    range_left, range_right = row.split(',')
    range_left, range_right = (
        [int(x) for x in range_left.split('-')],
        [int(x) for x in range_right.split('-')],
    )
    if (range_left[0] <= range_right[0] and range_left[1] >= range_right[0]) \
        or (range_right[0] <= range_left[0] and range_right[1] >= range_left[0]):
        total += 1

print(total)

# output: 886
assert total == 886
