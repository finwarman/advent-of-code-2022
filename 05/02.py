#! /usr/bin/env python3

import re

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = data.split('\n')[:-1]

# ==== SOLUTION ====

# get number of stacks
i = 0
while rows[i][1] != '1':
    i += 1

start_row = i + 2
stacks_count = int(rows[i][-1])
stacks = [[] for _ in range(stacks_count)]

# load stacks into array
for row in rows[0:stacks_count][::-1]:
    for i in range(0, len(row), 4):
        crate = row[i+1]
        if crate.strip():
            stacks[i//4].append(crate)

# rearrange stacks
for row in rows[start_row:]:
    count, start, end = [int(x) for x in re.split(r'[^\d]+', row)[1:]]
    segment = []
    for i in range(count):
        crate = stacks[start-1].pop()
        segment.append(crate)
    stacks[end-1].extend(segment[::-1])

result = ''.join([stack[-1] for stack in stacks])
print(result)

# output: LVMRWSSPZ
assert result == 'LVMRWSSPZ'
