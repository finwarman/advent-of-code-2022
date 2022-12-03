#! /usr/bin/env python3

import string

# ==== INPUT ====
data = ''
f = 'input.txt'
with open(f, 'r', encoding='UTF-8') as file:
    data = file.read()

rows = [row.strip() for row in data.split('\n')[:-1]]

# ==== SOLUTION ====

total = 0

for i in range(0, len(rows), 3):
    elf1, elf2, elf3 = set(rows[i]), set(rows[i+1]), set(rows[i+2])
    common = elf1.intersection(elf2.intersection(elf3)).pop()
    if common.islower():
        total += 1 + string.ascii_lowercase.index(common)
    else:
        total += 27 + string.ascii_uppercase.index(common)

print(total)

# output: 2581
assert total == 2581
