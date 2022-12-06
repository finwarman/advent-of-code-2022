#! /usr/bin/env python3

import re

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

line = rows[0]
result = None

marker_size = 14
for i in range(len(line)-marker_size):
    window = line[i:i+marker_size]
    if len(set(window)) == marker_size:
        result = i+marker_size
        break

print(result)

# output: 2178
assert result == 2178
