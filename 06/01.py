#! /usr/bin/env python3

# ==== INPUT ====

INPUT = 'input.txt'
with open(INPUT, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

line = rows[0]
result = None

for i in range(len(line)-4):
    window = line[i:i+4]
    if len(set(window)) == 4:
        result = i+4
        break

print(result)

# output: 1578
assert result == 1578
