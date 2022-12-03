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

for row in rows:
    comp1, comp2 = set(row[:len(row)//2]), set(row[len(row)//2:])
    common = comp1.intersection(comp2).pop()
    if common.islower():
        total += 1 + string.ascii_lowercase.index(common)
    else:
        total += 27 + string.ascii_uppercase.index(common)

print(total)

# output: 7850
assert total == 7850
